import heapq

def find_k_smallest(nums, k):
    return heapq.nsmallest(k, nums)
