

def find_first_occurrence(sorted_list, target):
    (left, right) = (0, (len(sorted_list) - 1))
    result = (- 1)
    while (left <= right):
        mid = ((left + right) // 2)
        if (sorted_list[mid] == target):
            result = mid
            right = (mid - 1)
        elif (sorted_list[mid] < target):
            left = (mid + 1)
        else:
            right = (mid - 1)
    return result
