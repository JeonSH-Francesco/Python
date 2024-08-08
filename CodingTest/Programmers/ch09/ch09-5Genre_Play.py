'''
스트리밍 사이트에서 장르별로 가장 많이 재생된 노래를 두 개씩 모아
베스트 앨범을 출시하려 합니다.
노래는 고유번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.

1. 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
2. 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
3. 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.

genres[i]는 고유번호가 i인 노래의 장르입니다.
plays[i]는 고유 번호가 i인 노래가 재생된 횟수입니다.

genres = ["classic","pop","classic","classic","pop"]
plays = [500, 600, 150, 800, 2500]
return [4,1,3,0]

장르별로 가장 많이 재생된 노래를 최대 두 개까지 모아 베스트 앨범을 출시하므로 2번 노래는 수록되지 않습니다.

'''

def solution(genres, plays):
    # 최종 결과를 저장할 리스트
    answer = []
    # 장르별로 노래의 고유번호와 재생횟수를 저장할 딕셔너리
    info = {}
    # 장르별 총 재생횟수를 저장할 딕셔너리
    gens = {}
    
    # 각 노래의 장르와 재생횟수를 순회하며 info와 gens 딕셔너리를 채움
    for idx, (gen, play) in enumerate(zip(genres, plays)):
        # info 딕셔너리에 해당 장르가 없다면 초기화
        if gen not in info:
            info[gen] = [(idx, play)]
        else : 
            info[gen].append((idx,play))
        # gens 딕셔너리에 해당 장르의 총 재생횟수 누적
        gens[gen] = gens.get(gen,0) + play
    
    # gens 딕셔너리를 재생횟수 기준으로 내림차순 정렬하여 장르를 순회
    for (gen, _) in sorted(gens.items(), key=lambda x:x[1], reverse=True):
        # 해당 장르의 노래들을 재생횟수 기준으로 내림차순 정렬하고 최대 두 개의 노래를 선택
        for (idx, _) in sorted(info[gen],key=lambda x:x[1], reverse=True)[:2]:
            answer.append(idx)
    
    return answer

# 예시 입력
genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

# 함수 실행
print(solution(genres, plays))  # [4, 1, 3, 0]
'''
변수 설명 및 변화 과정
info: 장르별로 노래의 고유번호와 재생횟수를 저장하는 딕셔너리입니다. 

첫 번째 노래: {"classic": [(0, 500)]}
두 번째 노래: {"classic": [(0, 500)], "pop": [(1, 600)]}
세 번째 노래: {"classic": [(0, 500), (2, 150)], "pop": [(1, 600)]}
네 번째 노래: {"classic": [(0, 500), (2, 150), (3, 800)], "pop": [(1, 600)]}
다섯 번째 노래: {"classic": [(0, 500), (2, 150), (3, 800)], "pop": [(1, 600), (4, 2500)]}

gens: 장르별 총 재생횟수를 저장하는 딕셔너리입니다.
첫 번째 노래: {"classic": 500}
두 번째 노래: {"classic": 500, "pop": 600}
세 번째 노래: {"classic": 650, "pop": 600}
네 번째 노래: {"classic": 1450, "pop": 600}
다섯 번째 노래: {"classic": 1450, "pop": 3100}

answer: 최종 결과를 저장하는 리스트입니다. 재생횟수가 많은 장르부터 정렬된 노래의 고유번호를 순서대로 추가합니다.
pop 장르: [4, 1] (pop 장르의 노래 중 재생횟수가 많은 두 곡)
classic 장르: [4, 1, 3, 0] (classic 장르의 노래 중 재생횟수가 많은 두 곡)
이제 print(solution(genres, plays))을 실행하면 [4, 1, 3, 0]이 출력됩니다.
'''
