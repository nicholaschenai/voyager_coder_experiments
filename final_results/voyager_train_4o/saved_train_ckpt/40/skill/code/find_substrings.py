

def find_substrings(input_string, word_list):
    result = []
    for word in word_list:
        if (word in input_string):
            result.append(word)
    return result
