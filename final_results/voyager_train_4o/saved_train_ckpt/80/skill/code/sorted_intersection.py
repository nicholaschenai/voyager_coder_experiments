

def sorted_intersection(list1, list2):
    (pointer1, pointer2) = (0, 0)
    result = set()
    while ((pointer1 < len(list1)) and (pointer2 < len(list2))):
        if (list1[pointer1] == list2[pointer2]):
            result.add(list1[pointer1])
            pointer1 += 1
            pointer2 += 1
        elif (list1[pointer1] < list2[pointer2]):
            pointer1 += 1
        else:
            pointer2 += 1
    return sorted(result)
