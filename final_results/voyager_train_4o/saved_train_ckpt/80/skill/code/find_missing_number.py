

def find_missing_number(nums):
    n = (len(nums) + 1)
    expected_sum = ((n * (n + 1)) // 2)
    actual_sum = sum(nums)
    missing_number = (expected_sum - actual_sum)
    return missing_number
