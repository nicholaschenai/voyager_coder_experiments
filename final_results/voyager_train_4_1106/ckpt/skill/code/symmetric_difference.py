

def symmetric_difference(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    sym_diff_set = (set1 ^ set2)
    return list(sym_diff_set)
