

def find_intersection(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    intersection_set = set1.intersection(set2)
    intersection_list = list(intersection_set)
    return intersection_list
