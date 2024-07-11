strings1=["sun","bed","car"]
strings2=["abcd","abce","cdx"]

def solution(strings,n):
    return sorted(sorted(strings),key=lambda x: x[n])


print(solution(strings1,1))
print(solution(strings2,2))
