def solution(n):
    res = [[0] * i for i in range(1, n+1)]
    # n값을 기반으로 2차원 리스트를 생성하고 초기값을 0으로 설정
    # 2차원 리스트 각 행의 길이는 1부터 n까지 순차적으로 증가
    # n=4 인 경우
    #res = [
    #[0],        i = 1
    #[0, 0],     i = 2
    #[0, 0, 0],  i = 3
    #[0, 0, 0, 0]  i = 4
    # ]

    y, x = -1, 0
    # 현재 위치를 나타내는 변수로 y=-1, x=0으로 세팅
    num = 1
    # 배열에 채워질 숫자를 나타내는 변수로 초기값 1로 세팅

    for i in range(n):
        for _ in range(i, n):
            angle = i % 3
            # 현재 패턴에서의 이동방향 결정하는 angle 변수
            # 순서대로 아래 -> 오른쪽 -> 위 (반시계 나선형)

            # 아래인 경우
            if angle == 0:
                y += 1
                print("i : %d angle: %d x: %d y: %d" % (i, angle, x, y))
                
            # 오른쪽인 경우
            elif angle == 1:
                x += 1
                print("i : %d angle: %d x: %d y: %d" % (i, angle, x, y))
                
            # 왼쪽, 대각선인 경우
            elif angle == 2:
                y -= 1
                x -= 1
                print("i : %d angle: %d x: %d y: %d" % (i, angle, x, y))
                
            # 최종 결과 생성
            res[y][x] = num
            print("i: %d res[%d][%d]: %d" % (i, y, x, num))
            print("\n")
            num += 1

    return [i for j in res for i in j]
    #for j in res : res 리스트의 각 원소 j에 대해 반복
    #res는 2차원 리스트 이므로 각 j는 하위 리스트를 나타낸다.
    #for i in j : 각 하위 리스트 j의 원소 i에 대해 반복
    #i는 각 원소 i를 선택한다.
    #2차원 리스트를 펼쳐서 1차원 리스트로 만들어 준다.
    
    #원리를 파악해 보길 바란다. 3차원 리스트 인 경우
    #return [i for j in three_dim_list for k in j for i in k ]
    
# n이 4, 5, 6인 경우의 출력 결과
output_4 = solution(4)
output_5 = solution(5)
output_6 = solution(6)

print(output_4) 
print(output_5)
print(output_6)

'''
출력 결과:
[1, 2, 9, 3, 10, 8, 4, 5, 6, 7]
[1, 2, 12, 3, 13, 11, 4, 14, 10, 5, 6, 7, 8, 9]
[1, 2, 15, 3, 16, 14, 4, 17, 13, 5, 18, 12, 6, 7, 8, 9, 10, 11]
'''
