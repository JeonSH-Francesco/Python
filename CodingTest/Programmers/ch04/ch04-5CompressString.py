def compress(s, length):
    words = [s[i:i+length] for i in range(0, len(s), length)]
    res = []
    cur_word = words[0]
    cur_cnt = 1
    
    for pattern, compare in zip(words, words[1:] + ['']):
    #pattern대로 자른 문자와 compare를 변수를 비교했을 때, 즉, words와 words[1:]을 비교했을 때, 끝까지!['']
        if pattern == compare:
            cur_cnt += 1
            #같은 경우 cur_cnt를 증가 시켜주고
        else:
            #다른 경우 res에 cur_word, cur_cnt값을 저장하고 cur_word는 compare로 초기화, cur_cnt는 1로 초기화를 한다.
            res.append([cur_word, cur_cnt])
            cur_word = compare
            cur_cnt = 1
        #그렇게 pattern대로 분할이 끝난 경우
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)
    #word cnt 즉, res에 저장된 부분을 계산하여 len(word)와 len(str(cnt)) 즉, 반복된 문자열에 대한 반복된 횟수를 더하여 반환해준다.    
'''
EX)
"aabbaccc",
"a"에서 "a"로 패턴이 일치하므로 cur_cnt를 2로 증가시킵니다.
"a"에서 "b"로 패턴이 변경되었으므로 "a"의 등장 횟수를 res에 추가하고 cur_word와 cur_cnt를 초기화합니다.
"b"에서 "b"로 패턴이 일치하므로 cur_cnt를 2로 증가시킵니다.
"b"에서 "a"로 패턴이 변경되었으므로 "b"의 등장 횟수를 res에 추가하고 cur_word와 cur_cnt를 초기화합니다.
"a"에서 "c"로 패턴이 변경되었으므로 "a"의 등장 횟수를 res에 추가하고 cur_word와 cur_cnt를 초기화합니다.
"c"에서 "c"로 패턴이 일치하므로 cur_cnt를 3으로 증가시킵니다.
이제 res에는 [['a', 2], ['b', 2], ['a', 1], ['c', 3]]와 같은 정보가 저장되어 있습니다. 이 정보를 활용하여 최종적으로 압축된 길이를 계산하게 됩니다.

'a'가 2회 등장하므로, 압축 후의 길이는 1 (len('a')) + 1 (len('2')) = 2가 됩니다.
'b'가 2회 등장하므로, 압축 후의 길이는 1 (len('b')) + 1 (len('2')) = 2가 됩니다.
'a'가 1회 등장하므로, 압축 후의 길이는 1 (len('a'))가 됩니다.
'c'가 3회 등장하므로, 압축 후의 길이는 1 (len('c')) + 1 (len('3')) = 2가 됩니다.
따라서 각각의 경우에서 압축 후의 길이는 2, 2, 1, 2가 됩니다. 이 값들을 모두 더하면 최종적으로 7이 됩니다.

'''
def solution(s):
    if len(s) == 1:
        return 1
    else:
        return min(compress(s, length) for length in range(1, len(s) // 2 + 1))

#압축 가능한 길이만큼 순회합니다.(len(s)//2=(전체의 1/2))+1(0인 경우 대비)

test_cases = [
    "aabbaccc",
    "ababcdcdababcdcd",
    "abcabcdede",
    "abcabcabcabcdededededede",
    "xababcdcdababcdcd",
]

for s in test_cases:
    result = solution(s)
    print(f"Input: {s}, Result: {result}")

'''
출력 결과
Input: aabbaccc, Result: 7
Input: ababcdcdababcdcd, Result: 9
Input: abcabcdede, Result: 8
Input: abcabcabcabcdededededede, Result: 14
Input: xababcdcdababcdcd, Result: 17
'''
