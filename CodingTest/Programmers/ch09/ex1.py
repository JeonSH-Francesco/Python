def has_duplicate_chars(s):
    char_set = set()

    for char in s:
        if char in char_set:
            return True
        char_set.add(char)
        

    return False

result = has_duplicate_chars("abcdefg")
print(result)

result = has_duplicate_chars("hello")
print(result)
