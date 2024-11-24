

def merge(left, right):
    sorted_list = []
    i = j = 0
    while ((i < len(left)) and (j < len(right))):
        if (left[i] < right[j]):
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list




def merge_sort(arr):
    if (len(arr) <= 1):
        return arr
    mid = (len(arr) // 2)
    left_half = arr[:mid]
    right_half = arr[mid:]
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)
    return merge(sorted_left, sorted_right)
