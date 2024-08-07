a1 = [6, 3, 9]
print('a1:', a1)
a2 = a1.sort() # 원본을 정렬하고 수정합니다(in-place)
print('-----정렬 후-----')
print('a1:', a1)
print('a2:', a2)

b1 = [6, 3, 9]
print('b1:', b1)
b2 = sorted(b1) # 원본은 유지하고 정렬한 새 리스트를 만듭니다
print('-----정렬 후-----')
print('b1:', b1)
print('b2:', b2)


#sort 함수는 리스트명,sort() 형식으로 "리스트 형의 메소드"이며 리스트 원본 값을 직접 수정합니다.
#sorted 함수는 sorted(리스트명) 형식으로 "내장함수"이며 리스트 원본 값은 그대로이고 정렬 값을 반환합니다.

'''
a1: [6, 3, 9]
-----정렬 후-----
a1: [3, 6, 9]
a2: None

특히 sort() 함수의 리턴 값이 None이므로 주의합니다. 정렬된 값은 리턴되지 않습니다.
원본 리스트 값이 정렬된 값으로 수정되었습니다.

b1: [6, 3, 9]
-----정렬 후-----
b1: [6, 3, 9]
b2: [3, 6, 9]

원본 리스트 b1 값은 유지되고 정렬된 새 리스트는 b2에 저장되었습니다.
'''
