import struct, socket
from datetime import datetime
import pygeoip

# GeoIP 데이터베이스 로드 (IP → 국가/도시 정보 조회용)
gi = pygeoip.GeoIP('GeoLiteCity.dat')

# MAC 주소 벤더 캐시 딕셔너리
mac_dict = {}

# TCP Follow Stream 저장용 딕셔너리
# key: (src_ip, src_port, dst_ip, dst_port) 튜플 → 하나의 TCP 세션을 식별
# value: 해당 세션의 payload 바이트 누적
tcp_streams = {}


class PacketHeader:
    """
    pcap 파일의 각 패킷 앞에 붙는 16바이트 헤더를 파싱하는 클래스
    구조: ts_sec(4) + ts_usec(4) + incl_len(4) + orig_len(4)
    """
    def __init__(self, data):
        offset = 0

        # 패킷 캡처 시각 (초, 마이크로초)
        # pcap 포맷은 little endian으로 저장됨
        self.ts_sec  = struct.unpack("<L", data[offset:offset + 4])[0]
        offset += 4
        self.ts_usec = struct.unpack("<L", data[offset:offset + 4])[0]
        offset += 4

        # 실제 파일에 저장된 패킷 길이 (캡처 제한에 의해 잘릴 수 있음)
        self.incl_len = struct.unpack("<L", data[offset:offset + 4])[0]
        offset += 4

        # 원본 패킷의 실제 길이 (네트워크 상 전송된 크기)
        self.orig_len = struct.unpack("<L", data[offset:offset + 4])[0]

        ts = str(self.ts_sec) + "." + str(self.ts_usec)
        print("Time stamp:", datetime.fromtimestamp(float(ts)),
              "| incl_len:", self.incl_len, "| orig_len:", self.orig_len)


class Ethernet:
    """
    이더넷 프레임을 파싱하는 클래스
    구조: dst_mac(6) + src_mac(6) + type(2) + payload
    """
    def __init__(self, data):
        offset = 0

        # 목적지 MAC 주소 (6바이트)
        self.dmac = data[offset:offset + 6].hex()
        offset += 6

        # 출발지 MAC 주소 (6바이트)
        self.smac = data[offset:offset + 6].hex()
        offset += 6

        print("Source MAC:", self.smac, "| Destination MAC:", self.dmac)

        # EtherType 필드 (2바이트)
        # 0x0008 (little endian) = 0x0800 → IPv4
        # 0x0608 (little endian) = 0x0806 → ARP
        self.ethernet_type = struct.unpack("<H", data[offset:offset + 2])[0]
        offset += 2

        if self.ethernet_type == 8:
            # EtherType이 0x0800(IPv4)인 경우 IP 파싱으로 넘김
            self.ip = IP(data[offset:])


class IP:
    """
    IPv4 헤더를 파싱하는 클래스
    구조: version+IHL(1) + DSCP(1) + total_len(2) + id(2) + flags+frag(2)
          + TTL(1) + protocol(1) + checksum(2) + src_ip(4) + dst_ip(4) + options
    """
    def __init__(self, data):

        # 첫 1바이트: 상위 4비트 = IP 버전, 하위 4비트 = IHL(헤더 길이)
        first_byte = bin(struct.unpack("<B", data[:1])[0]).replace("0b", "")
        first_byte = "0" * (8 - len(first_byte)) + first_byte  # 8비트로 패딩

        self.version       = first_byte[0:4]   # 상위 4비트: IP 버전 (IPv4 = 0100)
        self.header_length = first_byte[4:8]   # 하위 4비트: IHL (헤더 길이, 4바이트 단위)

        # TTL: 라우터를 몇 번 더 거칠 수 있는지 나타내는 값 (1바이트)
        self.ttl = struct.unpack("<B", data[8:9])[0]

        # 프로토콜 번호: 상위 레이어 프로토콜 식별 (1바이트)
        # 6 = TCP, 17 = UDP, 1 = ICMP
        self.proto_type = struct.unpack("<B", data[9:10])[0]

        # 출발지/목적지 IP 주소 (각 4바이트)
        # inet_ntop: 바이너리 → 점 표기 문자열 (예: 192.168.0.1)
        self.sip = socket.inet_ntop(socket.AF_INET, data[12:16])
        self.dip = socket.inet_ntop(socket.AF_INET, data[16:20])

        print("Source IP:", self.sip, "| Destination IP:", self.dip, "| TTL:", self.ttl)
        print("GeoIP SRC:", gi.record_by_addr(self.sip),
              "| GeoIP DST:", gi.record_by_addr(self.dip))

        # TCP인 경우 IP 헤더 이후 데이터를 TCP로 파싱
        # IHL 필드(4비트)는 4바이트 단위이므로 * 4 해야 실제 바이트 수
        if self.proto_type == 6:
            ip_header_len = int(self.header_length, 2) * 4
            TCP(data[ip_header_len:], self.sip, self.dip)


class TCP:
    """
    TCP 헤더를 파싱하고 Follow Stream 기능을 수행하는 클래스
    구조: src_port(2) + dst_port(2) + seq(4) + ack(4)
          + data_offset+reserved(1) + flags(1) + window(2) + checksum(2) + urgent(2)
    """
    def __init__(self, data, sip, dip):

        # 출발지/목적지 포트 (각 2바이트)
        # 포트 번호는 네트워크 바이트 오더(big endian)로 저장됨
        # → RFC 793에서 TCP 헤더 필드는 모두 big endian으로 정의
        # → 네트워크 프로토콜 표준(RFC)은 big endian(network byte order)을 사용
        self.sport = struct.unpack(">H", data[0:2])[0]
        self.dport = struct.unpack(">H", data[2:4])[0]

        # 시퀀스 번호 (4바이트)
        # TCP는 RFC 793 표준에 따라 big endian(network byte order)으로 정의됨
        # little endian("<L")으로 읽으면 바이트 순서가 뒤집혀 잘못된 값이 나옴
        self.seq_number = struct.unpack(">L", data[4:8])[0]

        # ACK 번호 (4바이트) - 마찬가지로 big endian
        self.ack_number = struct.unpack(">L", data[8:12])[0]

        # Data Offset 필드 파싱 (TCP 헤더 길이)
        # 12번째 바이트의 상위 4비트가 Data Offset
        # Data Offset은 TCP 헤더의 길이를 4바이트 단위로 나타냄
        # 예: Data Offset = 5 → 헤더 길이 = 5 * 4 = 20바이트 (기본 TCP 헤더)
        # * 8이 아닌 * 4인 이유: 필드 단위가 32비트(4바이트) 워드이기 때문
        data_offset_byte = bin(struct.unpack("<B", data[12:13])[0]).replace("0b", "")
        data_offset_byte = "0" * (8 - len(data_offset_byte)) + data_offset_byte
        data_offset_bits = "0" + data_offset_byte[0:3]  # 상위 4비트 추출 (앞에 0 패딩)
        self.header_length = int(data_offset_bits, 2) * 4  # 4바이트 단위 → 실제 바이트 수

        # 플래그 필드 (1바이트, 하위 6비트 사용)
        # URG | ACK | PSH | RST | SYN | FIN 순서
        flags_byte = bin(struct.unpack("<B", data[13:14])[0]).replace("0b", "")
        self.flags = "0" * (6 - len(flags_byte)) + flags_byte

        if self.flags[0] == "1":
            print("  [URG] Urgent")
        if self.flags[1] == "1":
            print("  [ACK] Acknowledge")
        if self.flags[2] == "1":
            print("  [PSH] Push")
        if self.flags[3] == "1":
            print("  [RST] Reset")
        if self.flags[4] == "1":
            print("  [SYN] Synchronize")
        if self.flags[5] == "1":
            print("  [FIN] Finish")

        print("Source Port:", self.sport, "| Destination Port:", self.dport)
        print("Seq:", self.seq_number, "| Ack:", self.ack_number)
        print("Flags:", self.flags)
        print("-----------------------------------\n")

        # TCP payload 추출 (헤더 이후 데이터)
        tcp_payload = data[self.header_length:]

        # ─────────────────────────────────────────────
        # TCP Follow Stream
        # ─────────────────────────────────────────────
        # 하나의 TCP 세션을 식별하는 키를 만들 때
        # (src→dst)와 (dst→src) 양방향을 동일 세션으로 묶기 위해
        # 항상 정렬된 튜플을 키로 사용
        stream_key = tuple(sorted([(sip, self.sport), (dip, self.dport)]))

        if stream_key not in tcp_streams:
            # 새로운 세션이면 딕셔너리에 초기화
            # direction_data: 방향별(src→dst, dst→src) payload를 따로 저장
            tcp_streams[stream_key] = {
                "forward":  b"",   # sip:sport → dip:dport 방향 데이터
                "backward": b"",   # dip:dport → sip:sport 방향 데이터
            }

        if len(tcp_payload) > 0:
            # 현재 패킷 방향 판별 후 해당 방향에 payload 누적
            # stream_key는 정렬된 튜플이므로 첫 번째 원소와 비교해 방향 결정
            if (sip, self.sport) == stream_key[0]:
                tcp_streams[stream_key]["forward"]  += tcp_payload
            else:
                tcp_streams[stream_key]["backward"] += tcp_payload

        # HTTP 평문 패킷 출력 (포트 80)
        if len(tcp_payload) > 0 and (self.sport == 80 or self.dport == 80):
            try:
                decoded = tcp_payload.decode("utf-8")
                if decoded.startswith("GET ") or decoded.startswith("POST "):
                    if decoded.endswith("\r\n\r\n"):
                        print("[HTTP Request]\n", decoded)
            except:
                pass


def print_tcp_streams():
    """
    수집된 모든 TCP 스트림을 출력하는 함수
    pcap 파일을 전부 읽은 후 호출하면 Follow Stream 결과를 확인할 수 있음
    """
    print("\n========== TCP Follow Stream ==========")
    for idx, (key, stream) in enumerate(tcp_streams.items()):
        ep1, ep2 = key
        print(f"\n[Stream {idx}] {ep1[0]}:{ep1[1]} ↔ {ep2[0]}:{ep2[1]}")

        # Forward 방향 출력
        if stream["forward"]:
            print(f"  → Forward ({ep1[0]}:{ep1[1]} → {ep2[0]}:{ep2[1]}):")
            try:
                print(stream["forward"].decode("utf-8", errors="replace"))
            except:
                print(stream["forward"])

        # Backward 방향 출력
        if stream["backward"]:
            print(f"  ← Backward ({ep2[0]}:{ep2[1]} → {ep1[0]}:{ep1[1]}):")
            try:
                print(stream["backward"].decode("utf-8", errors="replace"))
            except:
                print(stream["backward"])

        print("---------------------------------------")



# pcap 파일을 바이너리로 읽기
fd = open("2.pcap", "rb")
data = fd.read()
fd.close()

offset = 0

# pcap 글로벌 헤더 24바이트 스킵
# 구조: magic_number(4) + version_major(2) + version_minor(2)
#        + thiszone(4) + sigfigs(4) + snaplen(4) + network(4)
global_header = data[offset:offset + 24]
offset += 24

packet_index = 0

while True:
    packet_index += 1
    print("-----------------------------------")
    print(f"Packet Index: {packet_index} / Offset: {offset:#x}")

    # 패킷 헤더 16바이트 파싱
    packet_header = PacketHeader(data[offset:offset + 16])
    offset += 16

    # 실제 패킷 데이터 추출 (incl_len 만큼)
    packet_data = data[offset:offset + packet_header.incl_len]
    offset += packet_header.incl_len

    # 이더넷 프레임 파싱 시작
    Ethernet(packet_data)

    # 파일 끝 도달 시 루프 종료
    if offset >= len(data):
        break

# 모든 패킷 파싱 완료 후 TCP Follow Stream 결과 출력
print_tcp_streams()


#2026.04.20 주석 자세히 추가 및 업데이트 작업 완료
