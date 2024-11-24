import heapq

def find_kth_largest(nums, k):
    min_heap = []
    for num in nums:
        if (len(min_heap) < k):
            heapq.heappush(min_heap, num)
        elif (num > min_heap[0]):
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, num)
    return heapq.heappop(min_heap)
