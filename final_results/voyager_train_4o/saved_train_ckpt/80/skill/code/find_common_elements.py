

def find_common_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    common_set = (set1 & set2)
    result = sorted(common_set)
    return result
