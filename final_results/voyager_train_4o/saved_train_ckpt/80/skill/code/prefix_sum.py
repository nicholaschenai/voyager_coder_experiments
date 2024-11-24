

def prefix_sum(nums):
    result = []
    cumulative_sum = 0
    for num in nums:
        cumulative_sum += num
        result.append(cumulative_sum)
    return result
