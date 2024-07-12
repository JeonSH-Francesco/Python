sample=[3,0,1,8,7,2,5,4,6,9]

def quickSort(data,low,high):
    p=data[(low+high)//2] #중간 값을 피벗으로 지정
    left, right = low, high #왼쪽과 오른쪽 인덱스를 초기화
    while True:
        while data[left]< p : left+=1 # 왼쪽부터 피벗보다 큰 값을 찾음
        while data[right]> p : right-=1 # 오른쪽부터 피벗보다 작은 값을 찾음
        if left>=right: break #왼쪽 인덱스가 오른쪽 인덱스보다 크거나 같아지면 종료
        data[left], data[right] = data[right], data[left]

    if low<right : quickSort(data,low,right) # 왼쪽 리스트 정렬
    if left< high : quickSort(data,right+1,high) #오른쪽 리스트 정렬

quickSort(sample,0,len(sample)-1)
print(sample)
