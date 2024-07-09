#H-index는 과학자의 생산성과 영향력을 나타내는 지표입니다. 어느 과학자의 H-index를 나타내는 값인 h를 구하려고 합니다.
#위키백과에 따르면, H-index는 다음과 같이 구합니다.
#어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-index입니다.
#어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations 가 매개변수로 주어질 때, 이 과학자의 H-index를 return 하도록 solution 함수를 작성해라
#제한 사항: 1~1000편 이하입니다. 논문별 인용횟수는 0회 이상 10000회 이하
#예)어느 과학자가 발표한 논문의 수는 5편이고, 그 중 3편의 논문은 3회 이상 인용되었고, 나머지 2편의 논문은 3회 이하 인용되었기 때문에, 이 과학자의 H-index :3


#citations=[3,0,6,1,5]-> return 3

#1.접근 방법 -> 전체 논문 갯수 n, 각 논문 당 인용된 횟수를 h라고 하면,
#2.첫 논문부터 n개의 논문까지 하나씩 비교하면서 현재 논문의 인용된 횟수 h보다 큰 논문의 개수가 h개 이상, 나머지 논문이 h번 이하를 참조한 경우를 찾는다.
#3.2번을 만족하는 h 중 가장 큰 값을 찾는다.

#오름차순 정렬 풀이
citations=[3,0,6,1,5]

def solution(citations):
    #오름차순 정렬 -> citations=[0,1,3,5,6]
    citations.sort()
    #idx는 논문의 인덱스, citation은 인용 횟수
    for idx, citation in enumerate(citations):
        #현재 논문의 인용 횟수(citation)가 남은 논문의 갯수보다 크거나 같은지 확인
        if citation >=len(citations) -idx:
            return len(citations) - idx
    #이 경우에는 (idx,citations) -> (0,0), (1,1), (2,3), (3,5), (4,6)이 될 것이다.
    #따라서 citation이 0,1,3,5,6이 될 것이고,
    # 0 >=5-0 False 이므로 계속 진행 1>=5-1=4도 마찬가지로 False이므로 계속 진행, 3>=5-2=3가 되어서 True이므로
    #3을 반환하게 된다.
    
    return 0# 조건을 만족하는 경우가 없다면 0을 반환합니다.


print(solution(citations))


'''
내림차순인 경우
def solution(citations):
    citations.sort(reverse=True)
    h_index = 0
    for i, c in enumerate(citations):
        if i < c:
            h_index = i + 1
        else:
            break
    return h_index

'''
