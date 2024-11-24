

def is_palindrome(s):
    normalized_str = s.lower()
    filtered_str = ''.join((char for char in normalized_str if char.isalnum()))
    return (filtered_str == filtered_str[::(- 1)])
