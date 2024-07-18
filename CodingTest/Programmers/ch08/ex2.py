def binary_search(target,data):
    start=0
    end=len(data)-1

    while start <= end:
        mid = (start+end)//2

        if data[mid] == target:
            return mid
        elif data[mid] < target:
            start = mid +1
        else:
            end = mid-1

    return None

data = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 7

result=binary_search(target,data)

if result is not None:
    print(f"타겟 값 {target}는 데이터 리스트의 인덱스 {result}에 있습니다.")
else:
    print(f"타겟 값{target}는 데이터 리스트에서 찾을 수 없습니다.")
