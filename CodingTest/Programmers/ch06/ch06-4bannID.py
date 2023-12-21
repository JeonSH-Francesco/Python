#제한 사항 : user_id 배열의 크기는 1이상 8이하입니다. user_id 배열 각 원소들의 값은 길이가 1이상 8이하인 문자열입니다.
#-응모한 사용자 아이디들은 서로 중복되지 않습니다. 응모한 사용자 아이디는 알파벳 소문자와 숫자만으로 구서되어 있습니다.
#banned_id 배열의 크기는 1이상 user_id 배열의 크기 이하입니다.
#banned_id 배열 각 원소들의 값은 길이가 1이상 8이하인 문자열입니다.
#불량 사용자 아이디는 알파벳 소문자와 숫자, 가리기 위한 문자 '*'로만 구성되어 있습니다.
#불량 사용자 아이디는 '*' 문자를 하나 이상 포함하고 있습니다.
#불량 사용자 아이디 하나는 응모자 아이디 중 하나에 해당하고 같은 응모자 아이디가 중복해서 제재 아이디 목록에 들어가는 경우는 없습니다.
#제재 아이디 목록들을 구했을 때, 아이디들이 나열된 순서와 관계없이 아이디 목록의 내용이 동일하다면 같은 것으로 처리하여 하나로 세면 됩니다.

import re

def search(idx, visit, userID, answer, banPatterns):
    if idx == len(banPatterns):
        answer.add(visit)
        return

    for i in range(len(userID)):
        if (visit & (1 << i) > 0 or not re.fullmatch(banPatterns[idx], userID[i])):
            continue
        #각 단어를 2진수로 만들고 or 와 and 연산으로 확인
        search(idx + 1, visit | (1 << i), userID, answer, banPatterns)

#이번 DFS는 재귀 함수를 사용해 개발할 것이므로 시작 조건과 종료 조건, 점화식이 필요합니다.
#시작 조건은 1번 과정에서 주어진 아이디에서 가장 첫 아이디를 검사하는 것으로 결정
#점화식은 다음 제재 아이디와 다음 방문 상태를 점검하여 규칙이 서로 일치하는지 확인 하는 과정
#종료 조건은 마지막 제재 아이디에 도달했을 때 기준으로 함

def solution(user_id, banned_id):
    answer = set() # 중복 데이터를 자동으로 배제하는 set 자료형을 사용
    #'*' 문자가 모든 글자하고 일치하는 단어이므로 '.'문자로 치환하여 정규표현식 사용
    ban_patterns = [x.replace('*', '.') for x in banned_id]
    search(0, 0, user_id, answer, ban_patterns)#적당하게 형태만 만들어 놓기

    return len(answer)

input_data = [
    (["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]),
    (["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]),
    (["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"])
]

for data in input_data:
    result = solution(data[0], data[1])
    print(f"Input: {data}, Output: {result}")

'''
1. (["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"])

가능한 불량 사용자 조합 찾기:
첫 번째 불량 사용자 아이디 'fr*d*'에 대해 가능한 사용자 아이디 조합: ['frodo', 'fradi']
두 번째 불량 사용자 아이디 'abc1**'에 대해 가능한 사용자 아이디 조합: ['abc123']
따라서 가능한 불량 사용자 조합은 ['frodo', 'fradi']와 ['abc123'] 두 가지이며, 총 2가지 경우가 가능합니다.


2. (['frodo', 'fradi', 'crodo', 'abc123', 'frodoc'], ['*rodo', '*rodo', '******'])

불량 사용자 아이디 목록을 정규표현식 패턴으로 변환:
'*rodo' → '.rodo'
'*rodo' → '.rodo'
'******' → '......'
가능한 불량 사용자 조합 찾기:
첫 번째 불량 사용자 아이디 '.rodo'에 대해 가능한 사용자 아이디 조합: ['frodo', 'crodo']
두 번째 불량 사용자 아이디 '.rodo'에 대해 가능한 사용자 아이디 조합: ['frodo', 'crodo', 'frodoc']
세 번째 불량 사용자 아이디 '......'에 대해 가능한 사용자 아이디 조합: ['frodo', 'fradi', 'crodo', 'abc123', 'frodoc']
따라서 가능한 불량 사용자 조합은 ['frodo', 'crodo']와 ['frodo', 'crodo', 'frodoc'] 두 가지이며, 총 2가지 경우가 가능합니다.

3. (["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"])

불량 사용자 아이디 목록을 정규표현식 패턴으로 변환:
'fr*d*' → 'fr.d.'
'*rodo' → '.rodo'
'******' → '......'
'******' → '......'
가능한 불량 사용자 조합 찾기:
첫 번째 불량 사용자 아이디 'fr*d*'에 대해 가능한 사용자 아이디 조합: ['frodo', 'fradi']
두 번째 불량 사용자 아이디 '*rodo'에 대해 가능한 사용자 아이디 조합: ['frodo', 'crodo']
세 번째 불량 사용자 아이디 '......'에 대해 가능한 사용자 아이디 조합: ['frodo', 'fradi', 'crodo', 'abc123', 'frodoc']
네 번째 불량 사용자 아이디 '......'에 대해 가능한 사용자 아이디 조합: ['frodo', 'fradi', 'crodo', 'abc123', 'frodoc']
따라서 가능한 불량 사용자 조합은 ['frodo', 'fradi'], ['frodo', 'crodo'], ['frodo', 'fradi', 'crodo', 'abc123', 'frodoc'] 세 가지이며, 총 3가지 경우가 가능합니다.
'''
