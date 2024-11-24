from collections import Counter

def find_pairs_with_sum(nums, target):
    from collections import Counter
    num_count = Counter(nums)
    unique_pairs = set()
    for num in nums:
        complement = (target - num)
        if (complement in num_count):
            if ((num == complement) and (num_count[num] < 2)):
                continue
            pair = (min(num, complement), max(num, complement))
            unique_pairs.add(pair)
    return sorted(list(unique_pairs))
