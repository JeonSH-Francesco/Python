'''
수많은 마라톤 선수들이 마라톤에 참여하였습니다.
단 한명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.
마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이
주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

입출력 예

participant                                     | completion                | return
["leo","kiki","eden"]                           | ["eden","kiki"]           | "leo"
["marina","josipa","nikola","vinko","filipa"]   | ["josipa","filipa","marina","nikola"] | "vinko"
["mislav","stanko","mislav","ana"] | ["stanko]  | ["stanko","ana","mislav"] | "mislav"

동명이인이 있다는 것, 완주하지 못한 사람은 단 한명만 존재한다는 것이 핵심

get() 메서드의 사용법
구문 : dictionary.get(key,default)
key : 찾고자 하는 딕셔너리의 키
default : 키가 딕셔너리에 없을 경우 반환할 기본 값. default : None

# 예제 딕셔너리
example_dict = {'apple': 2, 'banana': 3}

# get() 메서드를 사용하지 않고 딕셔너리 접근
print(example_dict['apple'])   # 2
print(example_dict['orange'])  # KeyError: 'orange' (키가 존재하지 않으므로 오류 발생)

# get() 메서드를 사용하여 딕셔너리 접근
print(example_dict.get('apple', 0))   # 2 (키가 존재하므로 해당 값을 반환)
print(example_dict.get('orange', 0))  # 0 (키가 존재하지 않으므로 기본값 0을 반환)


'''
def solution(participant, completion):
    answer = {}
    # 참가자 명단을 이용하여 딕셔너리에 이름별로 카운트를 증가시킵니다.
    for i in participant:
        answer[i] = answer.get(i, 0) + 1
    
    # 완주자 명단을 이용하여 딕셔너리에 이름별로 카운트를 감소시킵니다.
    for j in completion:
        answer[j] -= 1
    
    # 딕셔너리에서 값이 0이 아닌 이름을 찾습니다. 그것이 완주하지 못한 선수입니다.
    for k in answer:
        if answer[k]:
            return k

# 예제 테스트 케이스
participants_list = [
    (["leo", "kiki", "eden"], ["eden", "kiki"]),
    (["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]),
    (["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])
]

# 각 테스트 케이스를 실행하고 결과를 출력합니다.
for participant, completion in participants_list:
    print(f"participant: {participant}")
    print(f"completion: {completion}")
    print(f"result: {solution(participant, completion)}\n")
