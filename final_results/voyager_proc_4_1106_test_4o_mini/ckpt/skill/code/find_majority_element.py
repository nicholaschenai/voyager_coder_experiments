

def find_majority_element(nums):
    n = len(nums)
    count = {}
    for num in nums:
        count[num] = (count.get(num, 0) + 1)
    for (num, cnt) in count.items():
        if (cnt > (n / 2)):
            return num
    return None
