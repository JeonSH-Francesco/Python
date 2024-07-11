from itertools import permutations

numbers1=[6,10,2]
numbers2=[3,30,34,5,9]

def solution(numbers):
    return max(list(map(''.join,permutations([str(x) for x in numbers]))))
# numbers 리스트의 숫자들을 문자열로 변환하고, 모든 순열을 결합하여 가장 큰 값을 반환합니다.

print(solution(numbers1))
print(solution(numbers2))
