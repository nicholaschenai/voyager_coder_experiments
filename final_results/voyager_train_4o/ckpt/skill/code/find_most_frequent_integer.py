

def find_most_frequent_integer(int_list):
    frequency_counter = {}
    for num in int_list:
        if (num in frequency_counter):
            frequency_counter[num] += 1
        else:
            frequency_counter[num] = 1
    most_frequent = None
    max_count = 0
    for (num, count) in frequency_counter.items():
        if (count > max_count):
            max_count = count
            most_frequent = num
    return most_frequent
