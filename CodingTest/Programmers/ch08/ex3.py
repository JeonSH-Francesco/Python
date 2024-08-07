'''
n명이 입국심사를 위해 줄을 서서 기다리고 있다.
각 입국 심사대에 있는 심사관마다 심사하는데 걸리는 시간은 다릅니다.
처음에 모든 심사대는 비어 있습니다. 한 심사대에서는 동시에 한 명만 심사를 할 수 있습니다.
가장 앞에 서 있는 사람은 비어 있는 심사대로 가서 심사를 받을 수 있습니다.

하지만 더 빨리 끝나는 심사대가 있으면 기다렸다가 그곳으로 가서 심사를 받을 수도 있습니다.
모든 사람이 심사를 받는데 걸리는 시간을 최소로 하고 싶습니다.

입국 심사를 기다리는 사람 수 n, 각 심사관이 한 명을 심사하는데 걸리는 시간이 담긴 배열 times가 매개변수로
주어질 때, 모든 사람이 심사를 받는데 걸리는 시간의 최솟값을 return하도록 soulution 함수를 작성하세요.

n=6, times=[7,10] return 28
심사가 7분, 10분 걸리는데,
->가장 첫 두사람은 바로 심사를 받으러 갑니다.
7분이 되었을 때, 첫 번째 심사대가 비고 3번째 사람이 심사를 받습니다.
10분이 되었을 때, 두 번째 심사대가 비고 4번째 사람이 심사를 받습니다.
14분이 되었을 때, 첫 번째 심사대가 비고 5번째 사람이 심사를 받습니다.
20분이 되었을 때, 두 번째 심사대가 비고 6번째 사람이 심사를 받을 수도 있지만,
1분을 더 기다린 후, 첫 번째 심사대에서 입국 심사를 거치면, 30분이 아닌 28분에 심사를 끝낼 수 있으므로
reutrn 값은 28입니다.
'''


# 0분부터 가장 오래 걸리는 소요 시간을 시작과 끝으로 지정합니다.
# 시작과 끝의 중간 시간에서 최대 몇 명 심사할 수 있을지 계산합니다.
# 심사해야 할 사람의 숫자보다 많으면 끝의 크기를 줄이고, 적으면 시작의 크기를 줄여 이진 탐색을 수행합니다.

def solution(n, times):
    # 초기 변수 설정
    answer = 0
    left, right = 1, max(times) * n  # 최소 시간(left)은 1분, 최대 시간(right)은 가장 오래 걸리는 심사 시간 * 인원 수

    # 이진 탐색 시작
    while left <= right:
        mid = (left + right) // 2  # 중간 시간을 계산
        print(mid, end=') ')
        people = 0  # mid 시간 동안 심사할 수 있는 총 인원 수
        
        # 각 심사대에서 mid 시간 동안 몇 명을 심사할 수 있는지 계산
        for time in times:
            people += mid // time
            
            if people >= n:  # 필요한 인원 수 이상 심사할 수 있으면 반복 종료
                break

        # 필요한 인원 수 이상을 심사할 수 있으면 시간을 줄임
        if people >= n:
            answer = mid
            right = mid - 1
        # 필요한 인원 수를 심사할 수 없으면 시간을 늘림
        # else 해도 되는데, 보이기 위해서
        elif people < n:
            left = mid + 1
    
    return answer

print(solution(6, [7, 10]))  # 출력: 28


'''

주어진 예시(n=6, times=[7, 10])로 실행하면:

초기 상태: left = 1, right = 60 (6 * 10)
첫 번째 반복: mid = 30
첫 번째 심사대: 30 // 7 = 4명
두 번째 심사대: 30 // 10 = 3명
총 7명, 충분하므로 right를 29로 설정하고 answer를 30으로 업데이트

두 번째 반복: mid = 15
첫 번째 심사대: 15 // 7 = 2명
두 번째 심사대: 15 // 10 = 1명
총 3명, 부족하므로 left를 16으로 설정

세 번째 반복: mid = 22
첫 번째 심사대: 22 // 7 = 3명
두 번째 심사대: 22 // 10 = 2명
총 5명, 부족하므로 left를 23으로 설정

네 번째 반복: mid = 26
첫 번째 심사대: 26 // 7 = 3명
두 번째 심사대: 26 // 10 = 2명
총 5명, 부족하므로 left를 27로 설정

다섯 번째 반복: mid = 28
첫 번째 심사대: 28 // 7 = 4명
두 번째 심사대: 28 // 10 = 2명
총 6명, 충분하므로 right를 27로 설정하고 answer를 28로 업데이트

여섯 번째 반복: mid = 27
첫 번째 심사대: 27 // 7 = 3명
두 번째 심사대: 27 // 10 = 2명
총 5명, 부족하므로 left를 28로 설정

반복 종료 후 answer는 28입니다. 따라서 결과는 28입니다.
'''
