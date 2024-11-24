

def is_anagram(str1, str2):
    normalized_str1 = ''.join(filter(str.isalpha, str1.lower()))
    normalized_str2 = ''.join(filter(str.isalpha, str2.lower()))
    sorted_str1 = sorted(normalized_str1)
    sorted_str2 = sorted(normalized_str2)
    return (sorted_str1 == sorted_str2)
