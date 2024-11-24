

def first_recurring_character(s):
    seen_characters = {}
    for char in s:
        if (char in seen_characters):
            return char
        seen_characters[char] = True
    return None
