'''
    7
   3 8
  8 1 0
 2 7 4 4
4 5 2 6 5
triangle = [[7],[3,8],[8,1,0],[2,7,4,4],[4,5,2,6,5]]

result = 30

'''


def solution(triangle):
    dp = [[0, *t, 0] for t in triangle]  # 각 행에 좌우에 0을 추가하여 초기화된 dp 테이블 생성
    for i in range(1, len(triangle)):
        for j in range(1, i+2):
            dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])  # 이전 행의 두 인접 값 중 큰 값을 더함

    return max(dp[-1])  # 마지막 행에서 가장 큰 값을 반환

triangle = [[7],[3,8],[8,1,0],[2,7,4,4],[4,5,2,6,5]]
print(solution(triangle))  # 결과 출력
