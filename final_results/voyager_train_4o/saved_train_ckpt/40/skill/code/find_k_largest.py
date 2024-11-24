import heapq

def find_k_largest(nums, k):
    if (k > len(nums)):
        return sorted(nums, reverse=True)
    min_heap = []
    for num in nums:
        if (len(min_heap) < k):
            heapq.heappush(min_heap, num)
        elif (num > min_heap[0]):
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, num)
    return sorted(min_heap, reverse=True)
