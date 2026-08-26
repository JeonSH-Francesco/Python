pip install cryptography protobuf grpcio-tools scapy 수행할 것.

<img width="330" height="421" alt="image" src="https://github.com/user-attachments/assets/39ff4a35-c1b3-4dfe-8797-6d0dc0a50207" />


직렬화는 중간 계층일 뿐 암호화로직은 별도 구현됨.

프로젝트 1 : 보안 메시징

secure_envelope.proto → 왜 이렇게 필드를 나눴는가

```
syntax = "proto3";

package secure;

// 실제 전송되는 최종 데이터 단위
// - 평문(plaintext)은 절대 담기지 않고, 암호화된 결과만 직렬화 대상이 됨
message SecureEnvelope {
  string sender_id = 1;        // 발신자 식별자
  bytes ciphertext = 2;        // AES-GCM으로 암호화된 실제 데이터
  bytes nonce = 3;             // AES-GCM nonce (매 메시지마다 랜덤 생성, 재사용 금지)
  bytes auth_tag = 4;          // AES-GCM 인증 태그 (변조 감지)
  bytes signature = 5;         // Ed25519 전자서명 (발신자 인증 + 무결성)
  int64 timestamp = 6;         // 유닉스 타임스탬프 (재전송 공격 방지용)
  string nonce_id = 7;         // 메시지 고유 ID (재전송 공격 방지용, UUID)
}

// 키 교환 시 상대방에게 전달하는 공개키 번들
message PublicKeyBundle {
  string owner_id = 1;
  bytes signing_public_key = 2;     // Ed25519 공개키 (서명 검증용)
  bytes exchange_public_key = 3;    // X25519 공개키 (키 교환용)
}**

```

ciphertext만 담고 평문은 절대 필드로 만들지 않음. → 스키마 설계 단계에서부터 평문이 실수로 로그나 저장소에 남을 가능성을 원천 차단하는 방어적 설계

nonce, auth_tag, signature를 각각 별도 필드로 분리 - 만약 이걸 하나의 bytes blob으로 뭉쳤다면 파싱 로직에서 길이 계산 실수가 생길 여지가 있는데, Protobuf 필드 경계를 자동으로 관리해주므로 이런 파싱 버그 위험이 사라짐.

timestamp + nonce_id를 동시에 둔 이유 : timestamp만 쓰면 “허용 시간 내에 같은 메시지를 여러 번 보내는 재전송”이 가능하고 nonce_id만 쓰면 무한정 저장소가 쌓이기에 두개를 합쳐 일정시간 내에서만 중복 검사하는 실무적 절충안

Peer 클래스 — 키를 "역할별로" 분리한 이유

```python
signing_key: Ed25519PrivateKey    # 서명 전용
exchange_key: X25519PrivateKey    # 키 교환 전용
```

서명용 키와 암호화(키교환)용 키를 하나로 합치지 않고 분리한 것이 핵심입니다. 
실무 암호학에서 "키 재사용(key reuse)"은 대표적인 취약점 패턴입니다. 
서명 알고리즘과 키 교환 알고리즘이 같은 키를 공유하면, 한쪽 프로토콜의 약점이 다른 쪽으로 전이될 수 있습니다.
두 개의 독립된 키 쌍을 쓰는 것 자체가 "역할 분리(separation of duties)"라는 보안 원칙을 코드로 구현한 것입니다.

derive_shared_key() - HKDF의 Info 파라미터

```
info=b"secure-envelope-v1"
```

ECDH로 나온 원시 공유 비밀(shared_secret)을 바로 AES 키로 쓰지 않고 HKDF를 거치는데, 
이때 `info`에 프로토콜 이름과 버전을 박아넣는 걸 도메인 분리(domain separation)라고 합니다. 
나중에 같은 키 교환 결과를 다른 프로토콜(v2)에서도 쓰게 되더라도, 파생되는 실제 AES 키는 완전히 달라지도록 강제하는 안전장치입니다.

seal_message() — 서명 대상에 메타데이터를 포함시킨 이유

```python
signing_target = (
    envelope.sender_id.encode() + envelope.ciphertext + envelope.nonce
    + envelope.auth_tag + str(envelope.timestamp).encode() + envelope.nonce_id.encode()
)
```

암호문만 서명하고 `timestamp`나 `nonce_id`를 서명 대상에서 빼면, 공격자가 암호문은 그대로 두고 timestamp만 바꿔서 재전송 검사를 우회할 수 있습니다. 
그래서 "전송되는 모든 필드를 서명 대상에 포함시킨다"는 원칙을 지킴.(자주 지적되는 실수 중 하나(부분 서명)를 미리 막은 설계)

open_message() — 검증 순서가 왜 이 순서인가

```
서명 검증 → 재전송 검사 → 복호화
```

이 순서 자체가 의미가 있습니다.

1. 서명을 가장 먼저 검증해서, 위조된 메시지는 복호화 시도조차 하지 않고 즉시 버립니다 → 불필요한 연산(복호화)을 아끼는 최적화이자, "신뢰할 수 없는 입력을 최대한 빨리 걸러낸다"는 보안 원칙입니다.
2. 재전송 검사를 복호화보다 먼저 함으로써, 이미 처리한 메시지에 대해 매번 복호화 연산을 반복하지 않도록 합니다.
3. AES-GCM 자체도 `auth_tag`로 내부적으로 변조를 재검증하므로, 서명(발신자 인증) + GCM 태그(암호문 무결성)라는 이중 방어선이 만들어집니다.

main()의 공격 시나리오 — 왜 "일부러 공격"을 코드에 넣었나

```python
공격 시나리오 1 : 동일 메시지 재전송
공격 시나리오 2 : 암호문 변조(비트 플립)
```

보안 코드에서 가장 흔한 함정은 "정상 케이스만 테스트하고 끝내는 것"인데 여기서는 방어로직을 만드는 것에 그치지 않고 실제로 공격을 흉내내서 그 방어가 진짜로 작동하는지 자체 검증하도록 함.

**→ protobuf기반 보안 메시징 실습을 통한 의의 : protobuf는 직렬화 포맷일 뿐, 암호화를 대신 해주는게 아니다. 보안이 필요한 실무 시스템에서는 Protobuf메시지 안에 “암호화된 바이트(bytes)”를 담는 봉투(Envelope) 패턴을 쓴다.**

**기밀성 : X25519키 교환, AES-256-GCM 대칭 암호화**

**무결성/인증 : Ed25519 전자서명**

**재전송 공격 방지 : timestamp + nonce_id를 검증측에서 추적**
 
