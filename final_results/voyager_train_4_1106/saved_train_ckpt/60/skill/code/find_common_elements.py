

def find_common_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    common_elements_set = set1.intersection(set2)
    common_elements_list = list(common_elements_set)
    return common_elements_list
