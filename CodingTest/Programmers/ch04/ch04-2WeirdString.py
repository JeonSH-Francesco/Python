def solution(s):
    cnt = 0
    result = []

    for char in s:
        if char == ' ':
            cnt = 0
            result.append(' ')
        else:
            result.append(char.upper() if cnt % 2 == 0 else char.lower())
            cnt += 1

    return ''.join(result)

#조건 표현 식 : <참일 때 값> if <조건> else <거짓일 때 값>


s = "try hello world"
print(solution(s))

'''
출력 결과 : 
TrY HeLlO WoRlD

'''
