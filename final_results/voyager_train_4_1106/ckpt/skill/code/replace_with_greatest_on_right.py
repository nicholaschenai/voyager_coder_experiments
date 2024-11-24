

def replace_with_greatest_on_right(nums):
    result = ([0] * len(nums))
    max_so_far = (- 1)
    for i in range((len(nums) - 1), (- 1), (- 1)):
        (result[i], max_so_far) = (max_so_far, max(max_so_far, nums[i]))
    return result
