import time
import uuid
import secrets
from dataclasses import dataclass, field

from cryptography.hazmat.primitives.asymmetric.x25519 import (
    X25519PrivateKey, X25519PublicKey,
)
from cryptography.hazmat.primitives.asymmetric.ed25519 import (
    Ed25519PrivateKey, Ed25519PublicKey,
)
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.exceptions import InvalidSignature, InvalidTag

import secure_envelope_pb2 as pb


# ----------------------------------------------------------------------
# 1. 참가자(Peer) 정의: 각자 서명용 키쌍 + 키교환용 키쌍을 가진다
# ----------------------------------------------------------------------
@dataclass
class Peer:
    peer_id: str
    signing_key: Ed25519PrivateKey = field(default_factory=Ed25519PrivateKey.generate)
    exchange_key: X25519PrivateKey = field(default_factory=X25519PrivateKey.generate)

    def public_bundle(self) -> pb.PublicKeyBundle:
        """상대방에게 넘겨줄 공개키 번들 (Protobuf 메시지)"""
        bundle = pb.PublicKeyBundle()
        bundle.owner_id = self.peer_id
        bundle.signing_public_key = self.signing_key.public_key().public_bytes(
            encoding=serialization.Encoding.Raw,
            format=serialization.PublicFormat.Raw,
        )
        bundle.exchange_public_key = self.exchange_key.public_key().public_bytes(
            encoding=serialization.Encoding.Raw,
            format=serialization.PublicFormat.Raw,
        )
        return bundle

    def derive_shared_key(self, their_exchange_pub: bytes) -> bytes:
        """X25519 ECDH로 공유 비밀을 만들고, HKDF로 AES 키를 뽑아낸다."""
        peer_pub = X25519PublicKey.from_public_bytes(their_exchange_pub)
        shared_secret = self.exchange_key.exchange(peer_pub)
        return HKDF(
            algorithm=hashes.SHA256(),
            length=32,                       # AES-256 키 길이
            salt=None,
            info=b"secure-envelope-v1",      # 프로토콜/버전 바인딩(도메인 분리)
        ).derive(shared_secret)


# ----------------------------------------------------------------------
# 2. 재전송 공격 방지용 검증기
#    - 이미 처리한 nonce_id는 다시 받아도 거부
#    - 너무 오래된 timestamp도 거부 (시계 오차 허용 범위 지정)
# ----------------------------------------------------------------------
class ReplayGuard:
    def __init__(self, max_skew_seconds: int = 30):
        self._seen_nonce_ids: set[str] = set()
        self.max_skew_seconds = max_skew_seconds

    def check_and_register(self, nonce_id: str, timestamp: int) -> None:
        now = int(time.time())
        if abs(now - timestamp) > self.max_skew_seconds:
            raise ValueError("메시지 timestamp가 허용 범위를 벗어남 (재전송 의심)")
        if nonce_id in self._seen_nonce_ids:
            raise ValueError("이미 처리된 메시지 (재전송 공격 탐지됨)")
        self._seen_nonce_ids.add(nonce_id)


# ----------------------------------------------------------------------
# 3. 발신: 평문 -> AES-GCM 암호화 -> Ed25519 서명 -> Protobuf 직렬화
# ----------------------------------------------------------------------
def seal_message(sender: Peer, shared_key: bytes, plaintext: bytes) -> bytes:
    aesgcm = AESGCM(shared_key)
    nonce = secrets.token_bytes(12)                 # AES-GCM 표준 nonce 길이
    ct_with_tag = aesgcm.encrypt(nonce, plaintext, associated_data=None)
    ciphertext, auth_tag = ct_with_tag[:-16], ct_with_tag[-16:]

    envelope = pb.SecureEnvelope()
    envelope.sender_id = sender.peer_id
    envelope.ciphertext = ciphertext
    envelope.nonce = nonce
    envelope.auth_tag = auth_tag
    envelope.timestamp = int(time.time())
    envelope.nonce_id = str(uuid.uuid4())

    # 서명 대상 = 암호문 + 메타데이터 전체 (일부만 서명하면 변조 여지가 생김)
    signing_target = (
        envelope.sender_id.encode()
        + envelope.ciphertext
        + envelope.nonce
        + envelope.auth_tag
        + str(envelope.timestamp).encode()
        + envelope.nonce_id.encode()
    )
    envelope.signature = sender.signing_key.sign(signing_target)

    return envelope.SerializeToString()      # <-- 실제로 네트워크로 나가는 바이트열


# ----------------------------------------------------------------------
# 4. 수신: Protobuf 역직렬화 -> 서명 검증 -> 재전송 검사 -> 복호화
# ----------------------------------------------------------------------
def open_message(
    wire_bytes: bytes,
    sender_signing_pub: bytes,
    shared_key: bytes,
    replay_guard: ReplayGuard,
) -> bytes:
    envelope = pb.SecureEnvelope()
    envelope.ParseFromString(wire_bytes)

    # (1) 서명 검증 - 발신자 신원 확인 + 데이터 변조 여부 확인
    signing_target = (
        envelope.sender_id.encode()
        + envelope.ciphertext
        + envelope.nonce
        + envelope.auth_tag
        + str(envelope.timestamp).encode()
        + envelope.nonce_id.encode()
    )
    verify_key = Ed25519PublicKey.from_public_bytes(sender_signing_pub)
    try:
        verify_key.verify(envelope.signature, signing_target)
    except InvalidSignature:
        raise ValueError("서명 검증 실패 - 위조되었거나 손상된 메시지")

    # (2) 재전송 공격 검사
    replay_guard.check_and_register(envelope.nonce_id, envelope.timestamp)

    # (3) 복호화 (AES-GCM 자체도 auth_tag로 변조를 재검증함 - 이중 방어)
    aesgcm = AESGCM(shared_key)
    try:
        plaintext = aesgcm.decrypt(
            envelope.nonce, envelope.ciphertext + envelope.auth_tag, associated_data=None
        )
    except InvalidTag:
        raise ValueError("복호화 실패 - 암호문 또는 태그가 손상됨")

    return plaintext


# ----------------------------------------------------------------------
# 5. 데모 시나리오
# ----------------------------------------------------------------------
def main():
    alice = Peer("alice")
    bob = Peer("bob")

    # --- 키 교환 단계 (공개키만 Protobuf로 주고받음) ---
    alice_bundle = alice.public_bundle()
    bob_bundle = bob.public_bundle()

    alice_shared_key = alice.derive_shared_key(bob_bundle.exchange_public_key)
    bob_shared_key = bob.derive_shared_key(alice_bundle.exchange_public_key)
    assert alice_shared_key == bob_shared_key, "ECDH 공유키가 양측에서 일치해야 함"

    replay_guard = ReplayGuard(max_skew_seconds=30)

    # --- 정상 메시지 전송 ---
    plaintext = b"[Confidential] Q3 pipeline deploy key rotation schedule attached."
    wire_bytes = seal_message(alice, alice_shared_key, plaintext)
    print(f"[전송] 직렬화된 바이트 길이: {len(wire_bytes)} bytes (원문 대비 오버헤드 확인 가능)")

    received = open_message(
        wire_bytes,
        sender_signing_pub=alice_bundle.signing_public_key,
        shared_key=bob_shared_key,
        replay_guard=replay_guard,
    )
    print(f"[수신 성공] 복호화된 평문: {received.decode()}")

    # --- 공격 시나리오 1: 동일 메시지 재전송 ---
    try:
        open_message(
            wire_bytes,
            sender_signing_pub=alice_bundle.signing_public_key,
            shared_key=bob_shared_key,
            replay_guard=replay_guard,
        )
    except ValueError as e:
        print(f"[방어 성공] 재전송 공격 차단: {e}")

    # --- 공격 시나리오 2: 암호문 변조(비트 플립) ---
    tampered = pb.SecureEnvelope()
    tampered.ParseFromString(wire_bytes)
    tampered.nonce_id = str(uuid.uuid4())  # 재전송 검사는 우회
    tampered.timestamp = int(time.time())
    corrupted_ct = bytearray(tampered.ciphertext)
    corrupted_ct[0] ^= 0xFF                # 첫 바이트 변조
    tampered.ciphertext = bytes(corrupted_ct)
    # 서명은 갱신하지 않음 (공격자는 개인키가 없으므로 재서명 불가)
    try:
        open_message(
            tampered.SerializeToString(),
            sender_signing_pub=alice_bundle.signing_public_key,
            shared_key=bob_shared_key,
            replay_guard=ReplayGuard(),
        )
    except ValueError as e:
        print(f"[방어 성공] 변조된 메시지 차단: {e}")


if __name__ == "__main__":
    main()


'''
# 메시지 클래스 + gRPC 통신 스텁을 함께 생성하는 대표적인 형태
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. example.proto

요소의미 및 역할python -m특정 파이썬 모듈을 스크립트 실행 형태로 직접 호출합니다.
grpc_tools.protocgRPC 패키지(grpcio-tools)에 포함된 Protocol Buffer 컴파일러 엔진입니다.
-I.--proto_path=.의 단축형으로, 
임포트할 .proto 파일들을 찾기 시작할 루트 검색 경로를 현재 디렉토리(.)로 지정합니다.
--python_out=.컴파일 결과로 생성되는 파이썬 데이터 구조 클래스 파일(*_pb2.py)을 
현재 디렉토리(.)에 출력합니다.~~~.proto컴파일할 대상 프로토콜 버퍼 정의 파일 이름입니다.

python -m grpc_tools.protoc -I. --python_out=. secure_envelope.proto
'''