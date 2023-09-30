def solution(arr1, arr2):
    answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
    # answer는 행렬 곱셈 결과를 저장하기 위한 2차원 리스트
    #len(arr2[0])은 arr2의 열 수를 나타내며, 이 값은 answer의 열 수가 됩니다.
    #len(arr1)은 arr1의 행 수를 나타내며, 이 값은 answer의 행 수가 됩니다.
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            #k 변수를 통해 행렬 곱셈에서 중간 계산을 위한 인덱스로 arr1의 열 인덱스를 나타냄.
            for k in range(len(arr1[0])):
                answer[i][j] += (arr1[i][k] * arr2[k][j])
                #arr1[i][k]*arr2[k][j]를 곱하고 answer[i][j]에 더합니다.
                #곱셈의 결과가 answer에 저장
    return answer

arr1_1 = [[1, 4], [3, 2], [4, 1]]
arr2_1 = [[3, 3], [3, 3]]
result_1 = solution(arr1_1, arr2_1)

arr1_2 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
arr2_2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]
result_2 = solution(arr1_2, arr2_2)

print("Test Case 1:")
for row in result_1:
    print(row)

print("\nTest Case 2:")
for row in result_2:
    print(row)
'''
출력 결과 : 
Test Case 1:
[15, 15]
[15, 15]
[15, 15]

Test Case 2:
[22, 22, 11]
[36, 28, 18]
[29, 20, 14]
'''
