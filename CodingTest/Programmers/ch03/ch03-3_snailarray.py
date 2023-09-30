def solution(n):
    res = [[0] * i for i in range(1, n+1)]
    #2차원 리스트 각 행의 길이는 1부터 n까지 순차적으로 증가
    y, x = -1, 0
    #현재 위치를 나타내는 변수로 y=-1 x=0으로 세팅
    num = 1
    #배열에 채워질 숫자를 나타내는 변수로 초기값 1로 세팅
    
    for i in range(n):
        for _ in range(i, n):
            angle = i % 3
            #현재 패턴에서의 이동방향 결정하는 anlge 변수
            # 순서대로 아래 -> 오른쪽 -> 위 (반시계 나선형)
           
            #아래인 경우
            if angle == 0: y += 1
            #오른쪽인 경우
            elif angle == 1: x += 1   
            #왼쪽, 대각선인 경우
            elif angle == 2: y -= 1; x -= 1   
            #최종 결과 생성   
            res[y][x] = num
            num += 1
            
    return [i for j in res for i in j]

# n이 4, 5, 6인 경우의 출력 결과
output_4 = solution(4)
output_5 = solution(5)
output_6 = solution(6)

print(output_4)  # [1, 2, 9, 3, 10, 8, 4, 5, 6, 7]
print(output_5)  # [1, 2, 12, 3, 13, 11, 4, 14, 10, 5, 6, 7, 8, 9]
print(output_6)  # [1, 2, 15, 3, 16, 14, 4, 17, 13, 5, 18, 12, 6, 7, 8, 9, 10, 11]
