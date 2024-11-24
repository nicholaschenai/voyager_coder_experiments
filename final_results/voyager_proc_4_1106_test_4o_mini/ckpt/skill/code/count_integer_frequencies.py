

def count_integer_frequencies(int_list):
    count_dict = {}
    for num in int_list:
        if (num in count_dict):
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    return count_dict
