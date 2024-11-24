

def insertion_sort(original_list):
    sorted_list = []
    for number in original_list:
        index = 0
        while ((index < len(sorted_list)) and (sorted_list[index] < number)):
            index += 1
        sorted_list.insert(index, number)
    return sorted_list
