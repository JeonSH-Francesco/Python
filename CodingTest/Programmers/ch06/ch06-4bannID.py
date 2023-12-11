import re

def search(idx, visit, userID, answer, banPatterns):
    if idx == len(banPatterns):
        answer.add(visit)
        return

    for i in range(len(userID)):
        if (visit & (1 << i) > 0 or not re.fullmatch(banPatterns[idx], userID[i])):
            continue
        search(idx + 1, visit | (1 << i), userID, answer, banPatterns)

def solution(user_id, banned_id):
    answer = set()
    ban_patterns = [x.replace('*', '.') for x in banned_id]
    search(0, 0, user_id, answer, ban_patterns)

    return len(answer)

# Example usage
input_data = [
    (["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]),
    (["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]),
    (["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"])
]

for data in input_data:
    result = solution(data[0], data[1])
    print(f"Input: {data}, Output: {result}")
