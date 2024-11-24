import heapq

def find_kth_smallest(nums, k):
    if (k > len(nums)):
        return None
    min_heap = []
    for num in nums:
        heapq.heappush(min_heap, num)
    for _ in range((k - 1)):
        heapq.heappop(min_heap)
    return heapq.heappop(min_heap)
