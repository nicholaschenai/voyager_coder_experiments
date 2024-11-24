

def find_most_frequent_element(int_list):
    if (not int_list):
        return None
    frequency = {}
    for num in int_list:
        frequency[num] = (frequency.get(num, 0) + 1)
    max_count = 0
    most_frequent = None
    for (num, count) in frequency.items():
        if ((count > max_count) or ((count == max_count) and ((most_frequent is None) or (num < most_frequent)))):
            max_count = count
            most_frequent = num
    return most_frequent
