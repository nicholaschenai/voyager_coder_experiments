

def symmetric_difference(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    result_set = (set1 ^ set2)
    result_list = sorted(result_set)
    return result_list
