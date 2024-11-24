

def second_largest_unique(nums):
    unique_nums = set(nums)
    if (len(unique_nums) < 2):
        return None
    sorted_unique_nums = sorted(unique_nums, reverse=True)
    return sorted_unique_nums[1]
