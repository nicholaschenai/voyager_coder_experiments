

def count_pairs_with_difference(nums):
    unique_nums = set(nums)
    count = 0
    for num in unique_nums:
        if ((num + 2) in unique_nums):
            count += 1
        if ((num - 2) in unique_nums):
            count += 1
    return (count // 2)
