

def char_frequency_histogram(input_string):
    char_count = {}
    for char in input_string:
        lower_char = char.lower()
        if lower_char.isalpha():
            if (lower_char in char_count):
                char_count[lower_char] += 1
            else:
                char_count[lower_char] = 1
    return char_count
