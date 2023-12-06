import re
def solution(s):
    return len(s) in {4,6} and bool(re.match('^[0-9]*$',s))

#->문자열 s 길이가 4혹은 6이고 숫자로만 구성돼 있는지 확인해주는 함수로 solution 함수를 만들어라

#정규 표현식에 많이 쓰이는 문제(정규 표현식을 통해서 쓰임.)
#1. search(<표현식>,<검색할 문자열>) : 첫 번째로 일치하는 문자열 반환, 만약 없다면 None 반환
#2. match(<표현식>,<검색할 문자열>) : 문자의 시작 부분에서 일치하는 문자열을 반환, 만약 없다면 None 반환
#3. findall(<표현식>,<검색할 문자열>) : 검색할 문자에서 일치하는 모든 문자열을 배열 형태로 반환
#4. sub(<표현식>,<표현 함수>,<검색할 문자열>) : string의 replace와 동일한 동작으로 하며, 검색된 문자열을 표현함수로 대체

#https://docs.python.org/ko/3/library/re.html
print(solution("a234"))  # Should print False
print(solution("1234"))  # Should print True
