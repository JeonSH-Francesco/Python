def solution(s, n):
    result = []
    for char in s:
        if char.isalpha():  # 알파벳인 경우만 처리
            is_upper = char.isupper()  # 대문자 여부 저장
            char = char.lower()  # 먼저 전부 소문자로 변환
            char = chr(((ord(char) - ord('a') + n) % 26) + ord('a'))  # 이동 계산 후 다시 문자로 변환
            if is_upper:  # 원래 대문자였다면 다시 대문자로 변환
                char = char.upper()
        result.append(char)
    return ''.join(result)

# 테스트 케이스
print(solution("AB", 1))  # "BC"
print(solution("z", 1))   # "a"
print(solution("a B z", 4))  # "e F d"
