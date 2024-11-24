

def group_strings_by_length(strings):
    length_dict = {}
    for string in strings:
        length = len(string)
        if (length in length_dict):
            length_dict[length].append(string)
        else:
            length_dict[length] = [string]
    return length_dict
