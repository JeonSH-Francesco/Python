'''
카카오톡 단톡방 들어왔습니다. 나갔습니다. 문제
uid로 구분, id 변경 시 반영하도록 하는 문제

{<유저 아이디>:<유저 닉네임>}

입출력 예시 
record = ["Enter uid 1234 Muzi", "Enter uid 4567 Prodo",
"Leave uid 1234","Enter uid 1234 Prodo",
"Change uid 4567 Ryan"]

result = ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.",
"Prodo님이 나갔습니다.","Prodo님이 들어왔습니다."]

'''
def solution(record):
    answer = []  # 최종 출력 메시지를 저장할 리스트
    actions = []  # 각 이벤트를 (명령어, 사용자 아이디) 형태로 저장할 리스트
    user = {}  # 사용자 아이디(uid)를 키로 하고 닉네임을 값으로 저장할 딕셔너리

    for event in record:
        info = event.split()  # 이벤트를 공백 기준으로 분리
        cmd, uid = info[0], info[1]  # 명령어와 사용자 아이디 추출
        # 입장(Enter) 또는 닉네임 변경(Change)인 경우
        if cmd in ("Enter", "Change"):
            nick = info[2]  # 닉네임 추출
            user[uid] = nick  # 사용자 딕셔너리에 uid를 키로 하고 닉네임을 값으로 저장

        actions.append((cmd, uid))  # 명령어와 사용자 아이디를 actions 리스트에 저장

    for action in actions:
        cmd, uid = action  # 명령어와 사용자 아이디 추출
        if cmd == "Enter":
            answer.append(f"{user[uid]}님이 들어왔습니다.")  # 입장 메시지 추가
        elif cmd == "Leave":
            answer.append(f"{user[uid]}님이 나갔습니다.")  # 퇴장 메시지 추가

    return answer

# 예시 입력
record = [
    "Enter uid1234 Muzi", 
    "Enter uid4567 Prodo",
    "Leave uid1234",
    "Enter uid1234 Prodo",
    "Change uid4567 Ryan"
]

# 결과 출력
print(solution(record))
