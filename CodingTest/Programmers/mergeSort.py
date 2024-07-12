sample = [3, 0, 1, 8, 7, 2, 5, 4, 6, 9]

# 두 개의 정렬된 리스트를 병합하는 함수
def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:  # 왼쪽과 오른쪽 리스트가 모두 존재할 때까지 반복
        if left[0] <= right[0]:  # 왼쪽 리스트의 첫 번째 요소가 오른쪽 리스트의 첫 번째 요소보다 작거나 같으면
            result.append(left[0])  # 왼쪽 리스트의 첫 번째 요소를 결과 리스트에 추가
            left = left[1:]  # 왼쪽 리스트의 첫 번째 요소를 제거
        else:
            result.append(right[0])  # 오른쪽 리스트의 첫 번째 요소를 결과 리스트에 추가
            right = right[1:]  # 오른쪽 리스트의 첫 번째 요소를 제거

    # 두 리스트 중 하나가 비었으면 남은 요소들을 결과 리스트에 추가
    result.extend(left)
    result.extend(right)
    return result

# 병합 정렬 함수
def mergeSort(data):
    if len(data) <= 1:  # 리스트의 길이가 1 이하이면 이미 정렬된 상태
        return data
    mid = len(data) // 2  # 리스트를 반으로 나눌 중간 인덱스

    left = mergeSort(data[:mid])  # 왼쪽 반을 재귀적으로 병합 정렬
    right = mergeSort(data[mid:])  # 오른쪽 반을 재귀적으로 병합 정렬
    return merge(left, right)  # 정렬된 왼쪽 반과 오른쪽 반을 병합

print(mergeSort(sample))  # 정렬된 리스트 출력
