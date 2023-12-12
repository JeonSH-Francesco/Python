def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

result = are_anagrams("listen", "silent")
print(result)

result = are_anagrams("hello", "world")
print(result)
