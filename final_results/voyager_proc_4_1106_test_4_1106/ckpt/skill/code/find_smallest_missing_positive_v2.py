

def find_smallest_missing_positive(nums):
    positive_nums = set(filter((lambda x: (x > 0)), nums))
    smallest_missing = 1
    while (smallest_missing in positive_nums):
        smallest_missing += 1
    return smallest_missing
