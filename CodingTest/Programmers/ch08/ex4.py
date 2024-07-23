'''
지원자가 지원서에 입력한 4가지 정보와 획득한 코딩 테스트 점수를 하나의 문자열로 구성한 값의 배열 info,
개발팀이 궁금해하는 문의 조건이 문자열 형태로 담긴 배열 query가 매개변수로 주어질 때,
각 문의 조건에 해당하는 사람들의 숫자를 순서대로 배열에 담아 return하도록 solution 함수를 완성해라.

제한 사항
개발 언어는 cpp, java, python 중 하나이다.
직군은 backend, frontend 중 하나이다.
경력은 junior, senior 중 하나이다.
소울 푸드는 chicken, pizza 중 하나이다.
점수는 코딩 테스트 점수를 의미하며 1~100,000이하입니다.
각 단어는 공백문자 하나로 구분되어 있습니다.

query 각 문자열은 "[조건]X" 형식입니다.

"cpp and - and senior and pizza 500"은 
"cpp로 코딩테스트를 봤으며, 경력은 senior이면서 소울 푸트는 pizza를 선택한 지원자 중 코딩테스트 점수를 500점이상 받은 사람은 모두 몇 명인가?"
를 의미합니다.
'''
def solution(info, query):
    # info 리스트의 각 문자열을 공백으로 나누어 2차원 리스트로 변환
    data = [i.split() for i in info]
    
    # query 조건들을 저장할 리스트 초기화
    queries = []

    # 각 쿼리에 대해 조건을 처리
    for q in query:
        # 쿼리를 공백으로 나누어 리스트로 변환
        q = q.split()
        
        # 쿼리에서 'and'를 제거
        for _ in range(3):
            q.remove('and')
        
        # 쿼리 리스트를 queries 리스트에 추가
        queries.append(q)

    # 각 쿼리에 대한 결과를 저장할 리스트 초기화
    answer = [0] * len(query)

    # 쿼리와 지원자 정보를 비교
    for i in range(len(queries)):
        q = queries[i]

        #각 지원자 정보를 확인
        for info in data:
            #지원자 정보의 각 항목을 쿼리 조건과 비교
            for j in range(5):
                if q[j] == '-': continue
                #쿼리에서 '-'는 모든 값을 허용하므로 넘어감
                elif j ==4 and int(info[j]) >= int(q[j]):answer[i]+=1
                # 점수 조건일 경우, 지원자의 점수가 쿼리 조건의 점수 이상인지 확인
                elif info[j]!=q[j] : break
                # 항목이 다를 경우 일치하지 않으므로 비교 중지
    return answer

# Example usage with the provided data
info = [
    "java backend junior pizza 150",
    "python frontend senior chicken 210",
    "python frontend senior chicken 150",
    "cpp backend senior pizza 260",
    "java backend junior chicken 80",
    "python backend senior chicken 50"
]

query = [
    "java and backend and junior and pizza 100",
    "python and frontend and senior and chicken 200",
    "cpp and - and senior and pizza 250",
    "- and backend and senior and - 150",
    "- and - and - and - 0"
]

result = solution(info, query)
print(result)  # Output: [1, 1, 1, 1, 6]


'''
예제 실행 결과 설명:
"java and backend and junior and pizza 100" 조건에 맞는 지원자는 1명입니다. (java backend junior pizza 150)
"python and frontend and senior and chicken 200" 조건에 맞는 지원자는 1명입니다. (python frontend senior chicken 210)
"cpp and - and senior and pizza 250" 조건에 맞는 지원자는 1명입니다. (cpp backend senior pizza 260)
"- and backend and senior and - 150" 조건에 맞는 지원자는 1명입니다. (cpp backend senior pizza 260)
"- and - and - and - 0" 조건에 맞는 지원자는 모든 지원자이므로 6명입니다.

'''
