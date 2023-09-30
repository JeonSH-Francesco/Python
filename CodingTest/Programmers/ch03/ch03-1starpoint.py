def solution(line):
    pos, answer = [], []
    n = len(line)

    x_min = y_min = int(1e15)
    x_max = y_max = -int(1e15)

    for i in range(n):
        a, b, e = line[i]
        for j in range(i + 1, n):
            c, d, f = line[j]
            if a * d == b * c:
                continue

            x = (b * f - e * d) / (a * d - b * c)
            y = (e * c - a * f) / (a * d - b * c)

            if x == int(x) and y == int(y):
                x = int(x)
                y = int(y)
                pos.append([x, y])
                if x_min > x:
                    x_min = x
                if y_min > y:
                    y_min = y
                if x_max < x:
                    x_max = x
                if y_max < y:
                    y_max = y

    x_len = x_max - x_min + 1
    y_len = y_max - y_min + 1
    coord = [['.'] * x_len for _ in range(y_len)]

    for star_x, star_y in pos:
        nx = star_x + abs(x_min) if x_min < 0 else star_x - x_min
        ny = star_y + abs(y_min) if y_min < 0 else star_y - y_min
        coord[ny][nx] = '*'

    for result in coord:
        answer.append(''.join(result))

    return answer[::-1]

# 테스트 케이스 입력
test_cases = [
    [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]],
    [[0, 1, -1], [1, 0, -1], [1, 0, 1]],
    [[1, -1, 0], [2, -1, 0]],
    [[1, -1, 0], [2, -1, 0], [4, -1, 0]]
]

# 각 테스트 케이스에 대해 결과 출력
for idx, test_case in enumerate(test_cases):
    print(f"Test Case {idx + 1}:")
    result = solution(test_case)
    for line in result:
        print(line)
    print()

'''
#교점에 별 만들기 - Level2
#문제 풀이 흐름
#1. 주어진 직선에서 교점을 구합니다.
#2. 그 중 정수 교점만 따로 변수로 저장합니다.
#3. 교점을 모두 표현할 수 있는 최소한의 사각형을 알아냅니다.
#4. 모든 교점을 *로 찍어서 표현합니다.
#5. 배열을 거꾸로 뒤집어 반환합니다.

def solution(line):
    #prevent swallow copy
    pos, answer = [], []
    #pos는 정수의 교점을 저장하기 위한 리스트
    #answer는 최종 결과를 저장하기 위한 리스트
    n = len(line)
    #입력으로 주어진 line 리스트의 길이를 n에 저장
    
    x_min = y_min = int(1e15)
    x_max = y_max = -int(1e15)
    #1e15는 1에 10^15를 곱한 값으로 초기화
    #이 변수들을 통해서 교점의 좌표 범위를 추적하는데 사용
    
    for i in range(n):
        a, b, e = line[i]
        for j in range(i + 1, n):
            c, d, f = line[j]
            if a * d == b * c:
                continue
            #평행선인 경우 다시 continue    
            x = (b*f - e*d) / (a*d - b*c)
            y = (e*c - a*f) / (a*d - b*c)
            #연립방정식으로 x,y 값 구하기
            #해당 교점이 정수인 경우에만 pos 리스트에 값을 저장하기
            if x == int(x) and y == int(y):
                x = int(x)
                y = int(y)
                pos.append([x,y])
                if x_min > x: x_min = x
                if y_min > y: y_min = y
                if x_max < x: x_max = x 
                if y_max < y: y_max = y 
    #최소한의 사각형의 크기를 계산
    x_len = x_max - x_min + 1
    y_len = y_max - y_min + 1
    coord = [['.'] * x_len for _ in range(y_len)]
    #리스트 초기화 : 초기값은 .로 표시
    #교점에 * 표시
    for star_x, star_y in pos:
        nx = star_x + abs(x_min) if x_min < 0 else star_x - x_min
        ny = star_y + abs(y_min) if y_min < 0 else star_y - y_min
        coord[ny][nx] = '*'
        
    for result in coord: answer.append(''.join(result))
    #최종적으로, answer 리스트에 coord 리스트를 거꾸로 뒤집어서 추가
    #이렇게 하면 결과 그림이 원래의 상하 반전된 형태로 반환
    return answer[::-1]
'''
