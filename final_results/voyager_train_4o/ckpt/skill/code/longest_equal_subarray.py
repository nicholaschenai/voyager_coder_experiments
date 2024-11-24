

def longest_equal_subarray(arr):
    if (not arr):
        return 0
    max_length = 1
    current_length = 1
    for i in range(1, len(arr)):
        if (arr[i] == arr[(i - 1)]):
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 1
    max_length = max(max_length, current_length)
    return max_length
