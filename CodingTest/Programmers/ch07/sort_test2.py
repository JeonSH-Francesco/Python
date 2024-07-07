#학점 기준으로 오름차순 정렬, 값이 같으면 성적순으로 오름차순 정렬
#비교 함수를 만들어서 두 값을 서로 비교한 다음, 결과에 따라 숫자를 반환하도록 하는 정렬 기준

from functools import cmp_to_key

students=[('kim','B+',18),('lee','A+',21),('jeong','A',18)]

def new_sort(n1,n2):
    if n1[2] > n2[2]: return 1
    elif n1[2]==n2[2]: return 0
    else : return -1


print(sorted(students,key=cmp_to_key(new_sort)))
