

def find_max_index(nums):
    if (not nums):
        return (- 1)
    max_value = nums[0]
    max_index = 0
    for index in range(len(nums)):
        if (nums[index] > max_value):
            max_value = nums[index]
            max_index = index
    return max_index
