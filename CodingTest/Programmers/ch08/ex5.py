'''
출발 지점부터 distance 만큼 떨어진 곳에 도착 지점이 있습니다.
그리고 그 사이에는 바위들이 놓여 있습니다.
바위 중 몇 개를 제거하려고 합니다.

예를 들어, 도착 지점이 25만큼 떨어져 있고, 바위가 [2, 14, 11, 21, 17] 지점에 놓여있을 때
바위 2개를 제거하면 출발 지점, 도착 지점, 바위간 거리는 아래와 같습니다.

[2, 14, 11, 21, 17]
-> [2, 11, 14, 17, 21]

제거한 바위 위치  | 각 바위 사이 거리 | 거리의 최솟 값
[21,17]          | [2, 9, 3, 11]    | 2
[2, 21]          | [11, 3, 3, 8]    | 3
[2, 11]          | [14, 3, 4, 4]    | 3
[11, 21]         | [2, 12, 3, 8]    | 2
[2, 14]          | [11, 6, 4, 4]    | 4

출발지점부터 도착지점까지 거리 distance, 바위들이 있는 위치를 담은 배열 rocks, 제거할 바위의 수 n이 매개변수
위에서 구한 거리의 최솟값 중에 가장 큰 값은 4
-> 최솟값들 중에 최댓값을 return 하도록 solution 함수를 작성

입출력 예
distance : 25  / rocks : [2, 14, 11, 21, 17] / n = 2 / return 4

'''
def solution(distance, rocks, n):
    answer = 0
    start, end = 0, distance

    # 바위들의 위치를 오름차순으로 정렬합니다.
    rocks.sort()

    # 가능한 최소 거리를 이진 탐색을 통해 찾습니다.
    while start <= end:
        mid = (start + end) // 2  # 중간값(가능한 최소 거리)을 계산합니다.
        del_stones = 0  # 제거한 바위의 개수를 세는 변수입니다.
        pre_stone = 0  # 마지막으로 고려한 바위의 위치를 저장하는 변수입니다. 초기값은 출발 지점입니다.

        # 각 바위의 위치를 확인하여 최소 거리 'mid'를 유지할 수 있는지 확인합니다.
        for rock in rocks:
            if rock - pre_stone < mid:  # 현재 바위와 마지막 바위 사이의 거리가 'mid'보다 작으면
                del_stones += 1  # 이 바위를 제거해야 합니다.
            else:
                pre_stone = rock  # 그렇지 않으면 다음 바위로 이동합니다.

            if del_stones > n:  # 제거한 바위의 개수가 허용된 개수를 초과하면 반복을 중단합니다.
                break

        # 제거한 바위의 수에 따라 이진 탐색 범위를 조정합니다.
        if del_stones > n:
            end = mid - 1  # 너무 많은 바위를 제거했으므로 가능한 최소 거리를 줄입니다.
        else:
            answer = mid  # 현재 가능한 최소 거리를 정답 후보로 저장합니다.
            start = mid + 1  # 더 큰 최소 거리를 시도합니다.

    return answer

print(solution(25, [2, 14, 11, 21, 17], 2))  # 출력: 4

'''
예제:
distance: 25
rocks: [2, 14, 11, 21, 17]
n: 2
초기화 및 정렬:
answer = 0
start = 0
end = 25
rocks.sort() -> rocks = [2, 11, 14, 17, 21]
이진 탐색 단계별로 살펴보기:
첫 번째 이진 탐색:
중간값 계산:

mid = (start + end) // 2 = (0 + 25) // 2 = 12
바위 제거 검사:

초기 상태: del_stones = 0, pre_stone = 0
바위 2: 2 - 0 = 2 < 12 -> del_stones = 1 (제거)
바위 11: 11 - 0 = 11 < 12 -> del_stones = 2 (제거)
바위 14: 14 - 0 = 14 >= 12 -> pre_stone = 14
바위 17: 17 - 14 = 3 < 12 -> del_stones = 3 (제거)
바위 21: 21 - 14 = 7 < 12 -> del_stones = 4 (제거)
바위 제거 수가 2를 초과하므로 del_stones > n.

범위 조정:

end = mid - 1 = 12 - 1 = 11
두 번째 이진 탐색:
중간값 계산:

mid = (start + end) // 2 = (0 + 11) // 2 = 5
바위 제거 검사:

초기 상태: del_stones = 0, pre_stone = 0
바위 2: 2 - 0 = 2 < 5 -> del_stones = 1 (제거)
바위 11: 11 - 0 = 11 >= 5 -> pre_stone = 11
바위 14: 14 - 11 = 3 < 5 -> del_stones = 2 (제거)
바위 17: 17 - 11 = 6 >= 5 -> pre_stone = 17
바위 21: 21 - 17 = 4 < 5 -> del_stones = 3 (제거)
바위 제거 수가 2를 초과하므로 del_stones > n.

범위 조정:

end = mid - 1 = 5 - 1 = 4

세 번째 이진 탐색:
중간값 계산:

mid = (start + end) // 2 = (0 + 4) // 2 = 2
바위 제거 검사:

초기 상태: del_stones = 0, pre_stone = 0
바위 2: 2 - 0 = 2 >= 2 -> pre_stone = 2
바위 11: 11 - 2 = 9 >= 2 -> pre_stone = 11
바위 14: 14 - 11 = 3 >= 2 -> pre_stone = 14
바위 17: 17 - 14 = 3 >= 2 -> pre_stone = 17
바위 21: 21 - 17 = 4 >= 2 -> pre_stone = 21
바위 제거 수가 2 이하이므로 del_stones <= n.

범위 조정:

answer = mid = 2
start = mid + 1 = 2 + 1 = 3

네 번째 이진 탐색:
중간값 계산:

mid = (start + end) // 2 = (3 + 4) // 2 = 3
바위 제거 검사:

초기 상태: del_stones = 0, pre_stone = 0
바위 2: 2 - 0 = 2 < 3 -> del_stones = 1 (제거)
바위 11: 11 - 0 = 11 >= 3 -> pre_stone = 11
바위 14: 14 - 11 = 3 >= 3 -> pre_stone = 14
바위 17: 17 - 14 = 3 >= 3 -> pre_stone = 17
바위 21: 21 - 17 = 4 >= 3 -> pre_stone = 21
바위 제거 수가 2 이하이므로 del_stones <= n.

범위 조정:

answer = mid = 3
start = mid + 1 = 3 + 1 = 4

다섯 번째 이진 탐색:
중간값 계산:

mid = (start + end) // 2 = (4 + 4) // 2 = 4
바위 제거 검사:

초기 상태: del_stones = 0, pre_stone = 0
바위 2: 2 - 0 = 2 < 4 -> del_stones = 1 (제거)
바위 11: 11 - 0 = 11 >= 4 -> pre_stone = 11
바위 14: 14 - 11 = 3 < 4 -> del_stones = 2 (제거)
바위 17: 17 - 11 = 6 >= 4 -> pre_stone = 17
바위 21: 21 - 17 = 4 >= 4 -> pre_stone = 21
바위 제거 수가 2 이하이므로 del_stones <= n.

범위 조정:

answer = mid = 4
start = mid + 1 = 4 + 1 = 5
종료 조건:
start > end가 되어 이진 탐색이 종료됩니다.

최종 결과:
answer = 4
따라서, 주어진 예제에서 최솟값들 중에 최댓값은 4가 됩니다.




'''
