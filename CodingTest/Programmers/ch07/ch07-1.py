from itertools import combinations
sample1=[2,1,3,4,1]
sample2=[5,0,2,7]

#itertools란 효율적인 루핑을 위한 이터레이터를 만드는 라이브러리로 여러가지 함수들이 많이 있지만, 그 중 combinations(), combinations_with_replacement(), product(), permutations()이 있다.


def solution(numbers):
    #중복을 제거하는 가장 쉬운 방법 : set
    answer = set()
    
    selects=list(combinations(numbers,2))
    #selects-> list에서 2개의 원소로 이루어진 모든 조합을 생성하고 리스트로 변환하여 저장
  
    for select in selects:
        #조합된 두개의 원소를 a와 b로 분리하고  
        (a,b) = select
        #a+b 두 원소의 합을 answer 집합에 추가합니다.
        answer.add(a+b)
        
    return sorted(answer)
#정렬된 answer를 반환합니다.

print(solution(sample1))
print(solution(sample2))
