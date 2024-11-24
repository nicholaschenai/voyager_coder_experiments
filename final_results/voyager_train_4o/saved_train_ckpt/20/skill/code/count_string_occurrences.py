

def count_string_occurrences(string_list):
    count_dict = {}
    for string in string_list:
        if (string in count_dict):
            count_dict[string] += 1
        else:
            count_dict[string] = 1
    return count_dict
