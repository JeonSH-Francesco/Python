def solution(s):
    answer = { } #dict 검색 비용은 O(1)이다.
    s =sorted(s[2:-2].split("},{"), key=len)
    for tuples in s:
        elements= tuples.split(',')
        for element in elements:
            number = int(element)
            if number not in answer:
                answer[number]=1   #dict 키 사용(value는 아무거나)
    return list(answer) #dict의 키 값만 배열의 인자가 됨

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))

'''
출력 결과 :
[2, 1, 3, 4]
[2, 1, 3, 4]
[111, 20]
[123]
[3, 2, 4, 1]

'''
