

def find_pair_with_sum(sorted_list, target_sum):
    left = 0
    right = (len(sorted_list) - 1)
    while (left < right):
        current_sum = (sorted_list[left] + sorted_list[right])
        if (current_sum == target_sum):
            return (sorted_list[left], sorted_list[right])
        elif (current_sum < target_sum):
            left += 1
        else:
            right -= 1
    return None
