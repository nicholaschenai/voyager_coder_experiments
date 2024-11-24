

def remove_vowels(input_string):
    vowels = 'aeiouAEIOU'
    result = []
    for char in input_string:
        if (char not in vowels):
            result.append(char)
    return ''.join(result)
