

def find_smallest_missing_positive(nums):
    positive_nums = set(filter((lambda x: (x > 0)), nums))
    i = 1
    while True:
        if (i not in positive_nums):
            return i
        i += 1
