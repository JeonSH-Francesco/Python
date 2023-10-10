import re
def solution(s):
    return re.sub('\d(?=\d{4})','*',s)

test_case=["01012345678","027778888"]

for s in test_case:
    result=solution(s)
    print(f"Input : {s}, Result : {result}")
