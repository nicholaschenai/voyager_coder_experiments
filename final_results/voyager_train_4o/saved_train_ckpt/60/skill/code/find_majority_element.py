

def find_majority_element(nums):
    n = len(nums)
    count = {}
    for num in nums:
        if (num in count):
            count[num] += 1
        else:
            count[num] = 1
    majority_threshold = (n / 2)
    for (num, cnt) in count.items():
        if (cnt > majority_threshold):
            return num
    return None
