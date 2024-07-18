def bisect(a,x,lo=0,hi=None):
    if lo <0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if a[mid] < x:
            lo = mid+1
        else:
            hi = mid
    return lo

'''
a: 정렬된 리스트.
x: 삽입하려는 요소.
lo: 탐색을 시작할 리스트의 최저 인덱스. 기본값은 0.
hi: 탐색을 끝낼 리스트의 최고 인덱스. 기본값은 None.

lo가 음수인 경우 예외 처리
hi가 None이면 리스트 a의 길이로 설정합니다.

lo가 hi보다 작을 때까지 반복합니다.
중간 인덱스 mid를 계산합니다.
a[mid]가 x보다 작으면 lo를 mid + 1로 설정합니다.
그렇지 않으면 hi를 mid로 설정합니다.

mylist는 [1, 2, 3, 7, 9, 11, 33] 입니다.
3을 삽입할 위치를 찾습니다.
함수는 2를 반환합니다. 이는 3이 이미 mylist의 인덱스 2에 있기 때문입니다.
'''

mylist=[1,2,3,7,9,11,33]
print(bisect(mylist,3))
