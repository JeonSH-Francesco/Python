def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer
#n을 통해서 역순으로 저장되고(3진법 계산)
#answer를 통해서 int(tmp,3)하면 tmp를 3진법으로 계산하여 출력하겠다는 의미
#예로 result = int('100', 2) -> print(result) =4 가 됩니다.
#int(a, b)에서는 두 개의 변수가 있습니다:
#a: 정수나 문자열로 표현된 숫자입니다. 이 값을 다른 진법에서 10진법으로 변환합니다.
#b: a의 현재 진법을 나타냅니다. 즉, a가 몇 진법인지를 지정합니다.
#따라서 int(a, b)는 a를 b진법에서 10진법으로 변환한 값을 반환하는 함수 호출입니다.

print(solution(45))  # Output: 7
print(solution(125))  # Output: 229
