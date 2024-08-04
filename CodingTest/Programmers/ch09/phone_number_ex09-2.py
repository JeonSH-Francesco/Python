'''
전화번호 목록문제
전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
전화번호가 다음과 같은 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

phone_book : ["119","97674223","1195524421"]
->return false

phoe_book : ["123","456","789"]
->return true 

phone_book : ["12","123","1235","567","88"]
->return false
'''

def solution(phone_book):
    headers = {}
    # 전화번호를 모두 딕셔너리에 등록합니다.
    for phone_number in phone_book:
        headers[phone_number] = 1

    # 각 전화번호의 접두사를 검사합니다.
    for phone_number in phone_book:
        header = ""
        for number in phone_number:
            header += number
            #print(header)
            #만들어질 접두사를 변수로 받아서 하나씩 딕셔너리에 등록합니다.
            #빈 문자열을 선언하고, 각 단어를 합쳐나가면서 나오는 결과물을 하나씩 딕셔너리에 등록합니다.
            # 현재 만들어진 접두사가 딕셔너리에 존재하고, 현재 전화번호 자체와 같지 않은 경우
            if header in headers and header != phone_number:
                return False
    return True

# 예제 테스트
print(solution(["119", "97674223", "1195524421"]))  # False
print(solution(["123", "456", "789"]))              # True
print(solution(["12", "123", "1235", "567", "88"])) # False


'''
1
11
119
9
97
976
9767
97674
976742
9767422
97674223
1
11
119
False
1
12
123
4
45
456
7
78
789
True
1
12
1
12
False

예를 들어, "1195524421"의 경우, header가 "1", "11", "119"로 점차 늘어나며 접두사가 생성됩니다. 
여기서 "119"는 이미 딕셔너리에 있는 "119"와 일치하고,
이것이 현재 전화번호 "1195524421"와 같지 않으므로 False를 반환하게 됩니다.


'''
