from itertools import product

def solution(word):
    # 'A', 'E', 'I', 'O', 'U'로 만들 수 있는 모든 조합을 생성합니다.
    data = [''.join(p) for i in range(1, 6) for p in product(['A', 'E', 'I', 'O', 'U'], repeat=i)]
    
    # 생성된 조합을 사전 순으로 정렬합니다.
    data.sort()
    
    try:
        # 주어진 단어가 정렬된 조합 리스트에서 어디에 위치하는지 찾아 반환합니다.
        answer = data.index(word) + 1
    except ValueError:
        # 단어가 리스트에 없는 경우 -1을 반환합니다.
        answer = -1
    
    return answer


print(solution("AAAAE"))  # 6
print(solution("AAAE"))   # 10
print(solution("I"))      # 1563
print(solution("EIO"))    # 1189

def find(data, p, step):
    #재귀 호출을 6단계까지 수행한 경우 함수를 종료합니다.
    if step == 6: return
    #현재까지 만들어진 문자열을 리스트에 추가합니다.
    if p != '': data.append(p)
    #모음들에 대하여 재귀 호출을 수행합니다.
    #p는 이전까지 생성된 문자열이며 c는 현재 루프에서 선택된 문자를 결합하여 새로운 문자열 생성
    for c in ['A', 'E', 'I', 'O', 'U']:
        find(data, ''.join([p, c]), step + 1)
        
def solution(word):
    answer = 0
    data = []
    #재귀 호출을 통해 모든 가능한 문자열을 생성합니다.
    find(data, '', 0)
    #주어진 단어가 몇 번째 인덱스에 해당하는지 찾습니다.
    for i in range(len(data)):
        if data[i] == word:
            answer = i + 1
            break
    
    return answer

print(solution("AAAAE"))  # 6
print(solution("AAAE"))   # 10
print(solution("I"))      # 1563
print(solution("EIO"))    # 1189
