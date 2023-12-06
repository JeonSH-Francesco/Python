def solution(n):
    res = [[0] * i for i in range(1, n + 1)]
    x, y = -1, 0
    num = 1

    for i in range(n):
        for _ in range(i, n):
            angle = i % 3
            if angle == 0:
                x += 1
            elif angle == 1:
                y += 1
            elif angle == 2:
                x -= 1
                y -= 1
            res[x][y] = num
            print("i: %d res[%d][%d]: %d" % (i, x, y, num))
            print("\n")
            num += 1
    #for j in res : res 리스트의 각 원소 j에 대해 반복
    #res는 2차원 리스트 이므로 각 j는 하위 리스트를 나타낸다.
    #for i in j : 각 하위 리스트 j의 원소 i에 대해 반복
    #i는 각 원소 i를 선택한다.
    #2차원 리스트를 펼쳐서 1차원 리스트로 만들어 준다.
    
    #원리를 파악해 보길 바란다. 3차원 리스트 인 경우
    #return [i for j in three_dim_list for k in j for i in k ]
    return [i for j in res for i in j]

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
