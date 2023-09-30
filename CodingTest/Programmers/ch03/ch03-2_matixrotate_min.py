def rotate(x1, y1, x2, y2, matrix):
    first = matrix[x1][y1]
    min_value = first
    
    # 왼쪽 출발 기준 -> y1 그대로
    for k in range(x1, x2):
        matrix[k][y1] = matrix[k+1][y1]
        min_value = min(min_value, matrix[k+1][y1])
    # 아래쪽 출발 기준 -> x2 그대로
    for k in range(y1, y2):
        matrix[x2][k] = matrix[x2][k+1]
        min_value = min(min_value, matrix[x2][k+1])
    # 오른쪽 출발 기준 -> y2 그대로
    for k in range(x2, x1, -1):
        matrix[k][y2] = matrix[k-1][y2]
        min_value = min(min_value, matrix[k-1][y2])
    # 위쪽 출발 기준 -> x1 그대로
    for k in range(y2, y1+1, -1):
        matrix[x1][k] = matrix[x1][k-1]
        min_value = min(min_value, matrix[x1][k-1])
    # matrix[x1][y1+1]까지 하는 이유는 first로 초기화 한 것이고 그 전까지 회전 및 할당을 해야 하기 때문  
    #즉, min_value 값을 회전 하면서 구한 후, return 
    matrix[x1][y1+1] = first
    return min_value

def solution(rows, columns, queries):
    matrix = [[(i)*columns+(j+1) for j in range(columns)] for i in range(rows)]
    #list comprehension으로 2차원 배열을 선언하고 세팅한다.
    result = []
    for query in queries:
        x1, y1, x2, y2 = query
        result.append(rotate(x1-1, y1-1, x2-1, y2-1, matrix))
        #-1을 하는 이유는 인덱스 시작 번호가 0부터이기 때문
    return result

# 예제 입력값
testcases = [
    (6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]),
    (3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]),
    (100, 97, [[1, 1, 100, 97]])
]

# 각 예제에 대한 결과 출력
for idx, (rows, columns, queries) in enumerate(testcases):
    result = solution(rows, columns, queries)
    print(f"Test {idx+1} 결과: {result}")


'''

Test 1 결과: [8, 10, 25]
Test 2 결과: [1, 1, 5, 3]
Test 3 결과: [1]
'''
