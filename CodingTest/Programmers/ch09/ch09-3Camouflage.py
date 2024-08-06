'''
스파이 위장 문제

clothes의 각 행은 [의상의 이름, 의상의 종류]로 이루어져 있습니다.
스파이가 가진 의상의 수는 1~30개 이하입니다.

clothes = [["yellowhat","headgear"], ["bluesunglasses","eyewear"], ["green_turban","headgear"]]
return 5

clothes = [["crowmask","face"], ["bluesunglasses","face"], ["smoky_makeup","face"]]
return 3


'''

def solution(clothes):
    answer = 1
    cloth_type = {}
    
    # 의상 종류별 개수 카운트
    for cloth, type in clothes:
        cloth_type[type] = cloth_type.get(type, 0) + 1
    
    # 각 의상 종류에서 하나를 선택하거나 선택하지 않는 경우를 고려
    for type in cloth_type:
        answer *= (cloth_type[type] + 1)
    
    # 아무 의상도 선택하지 않는 경우를 제외하기 위해 1을 빼줌
    return answer - 1

# 예시
print(solution([["yellowhat","headgear"], ["bluesunglasses","eyewear"], ["green_turban","headgear"]]))  # 출력: 5
print(solution([["crowmask","face"], ["bluesunglasses","face"], ["smoky_makeup","face"]]))  # 출력: 3


'''
예시를 통해 설명
입력: [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]

첫 번째 항목 ["yellowhat", "headgear"]
cloth = "yellowhat"
type = "headgear"
cloth_type.get("headgear", 0)는 0을 반환합니다 (처음 등장하는 type).
cloth_type["headgear"]를 1로 설정합니다.
결과: cloth_type = {"headgear": 1}

두 번째 항목 ["bluesunglasses", "eyewear"]
cloth = "bluesunglasses"
type = "eyewear"
cloth_type.get("eyewear", 0)는 0을 반환합니다 (처음 등장하는 type).
cloth_type["eyewear"]를 1로 설정합니다.
결과: cloth_type = {"headgear": 1, "eyewear": 1}

세 번째 항목 ["green_turban", "headgear"]
cloth = "green_turban"
type = "headgear"
cloth_type.get("headgear", 0)는 1을 반환합니다 (이미 headgear 키가 존재).
cloth_type["headgear"]를 2로 설정합니다.
결과: cloth_type = {"headgear": 2, "eyewear": 1}
요약
이 반복문은 clothes 리스트를 순회하면서 각 의상 종류별로 개수를 세어 cloth_type 딕셔너리에 저장합니다. 
이 딕셔너리는 최종적으로 각 의상 종류와 그 개수를 담고 있으며, 
이를 바탕으로 전체 조합의 경우의 수를 계산할 수 있습니다.

'''
