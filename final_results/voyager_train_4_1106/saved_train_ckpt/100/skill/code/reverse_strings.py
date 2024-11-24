

def reverse_strings(input_list):
    if (not input_list):
        return []
    reversed_list = []
    for string in input_list:
        reversed_list.append(string[::(- 1)])
    return reversed_list
