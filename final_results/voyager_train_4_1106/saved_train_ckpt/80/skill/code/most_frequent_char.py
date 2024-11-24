

def most_frequent_char(s):
    if (not s):
        return None
    frequency = {}
    for char in s:
        if (char in frequency):
            frequency[char] += 1
        else:
            frequency[char] = 1
    max_char = None
    max_count = 0
    for char in s:
        if (frequency[char] > max_count):
            max_count = frequency[char]
            max_char = char
    return max_char
