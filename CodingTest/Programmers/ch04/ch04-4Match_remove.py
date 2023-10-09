def solution(s):
    stack = []  # 스택 초기화
    for case in s:
        if stack and stack[-1] == case: # 스택의 가장 위에 있는 문자가 현재 문자와 같은지
            stack.pop()  # 스택에서 가장 위의 원소를 제거하여 짝을 이룸
        else:
            stack.append(case)  # 현재 문자를 스택에 추가
    return 0 if stack else 1  # 스택이 비어있으면 1 반환, 그렇지 않으면 0 반환

# 입력값과 결과값을 테스트
input_1 = "baabaa"
output_1 = solution(input_1)
print(f"Input: {input_1}, Output: {output_1}")

input_2 = "cdcd"
output_2 = solution(input_2)
print(f"Input: {input_2}, Output: {output_2}")
