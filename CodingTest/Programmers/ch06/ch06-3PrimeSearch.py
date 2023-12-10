from itertools import permutations

def checkPrime(n):
    # 소수인지 확인하는 함수
    if n < 2: 
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: 
            return False
    
    return True

def solution(numbers):
    answer = []
    numbers = list(numbers)
    
    # 가능한 모든 순열 생성
    num = []
    for i in range(1, len(numbers) + 1):
        num.append(list(permutations(numbers, i)))  

    # 순열을 정수로 변환하여 리스트에 추가
    num = [int(''.join(y)) for x in num for y in x]
    
    # 소수 여부 확인 후 소수인 경우 리스트에 추가
    for i in num:
        if checkPrime(i):
            answer.append(i)
    
    # 중복된 소수를 제거하고 개수 반환
    return len(set(answer))

# 테스트
result1 = solution("17")
result2 = solution("011")

# 결과 출력
print(f"Result for '17': {result1}")
print(f"Result for '011': {result2}")
