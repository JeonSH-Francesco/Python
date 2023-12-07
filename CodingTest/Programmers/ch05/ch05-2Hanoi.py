def hanoi(n,start,to,mid,answer):
    if n==1:
        return answer.append([start,to])
    hanoi(n-1, start,mid,to,answer)
    answer.append([start,to])
    hanoi(n-1,mid,to,start,answer)
    
def solution(n):
    answer=[]
    hanoi(n-1,1,3,2,answer)
    return answer

print(solution(2))
print(solution(3))
print(solution(4))

'''
hanoi 탑에서 원반 3개인 경우를 보면
(3,1,3,2)=(n,start,to,mid)라고 하면
->(2,1,2,3)=(n-1,start,mid,to) && (2,2,3,1)=(n-1,mid,to,start) 순으로 되는 부분을 확인할 수 있다.

-->(2,1,2,3)=(n,start,to,mid)기준으로 동일하게
--->(1,1,3,2)=(n-1,start,mid,to) && (1,3,2,1)=(n-1,mid,to,start)

-->(2,2,3,1)=(n,start,to,mid)기준으로 동일하게
--->(1,2,1,3)=(n-1,start,mid,to)&&(1,1,3,2)=(n-1,mid,to,start)
로 된다.

n=3  (3,1,3,2)
      |
      |
n=2  (2,1,2,3)-------------------(2,2,3,1)
      |                                  |
n=1   |---------------|                  |--------------------|
     (1,1,3,2)       (1,3,2,1)         (1,2,1,3)       (1,1,3,2)

출력 결과
[[1, 3]]
[[1, 2], [1, 3], [2, 3]]
[[1, 3], [1, 2], [3, 2], [1, 3], [2, 1], [2, 3], [1, 3]]
'''
