

def find_smallest_difference_pair(nums):
    nums.sort()
    min_diff = float('inf')
    closest_pair = (None, None)
    for i in range((len(nums) - 1)):
        diff = abs((nums[i] - nums[(i + 1)]))
        if (diff < min_diff):
            min_diff = diff
            closest_pair = (nums[i], nums[(i + 1)])
    return closest_pair
