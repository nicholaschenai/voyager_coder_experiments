

def longest_unique_substring(s):
    char_set = set()
    max_length = 0
    start = 0
    longest_substr = ''
    for end in range(len(s)):
        while (s[end] in char_set):
            char_set.remove(s[start])
            start += 1
        char_set.add(s[end])
        if (((end - start) + 1) > max_length):
            max_length = ((end - start) + 1)
            longest_substr = s[start:(end + 1)]
    return longest_substr
