import heapq

def find_k_largest(nums, k):
    max_heap = [(- num) for num in nums]
    heapq.heapify(max_heap)
    largest_elements = []
    for _ in range(min(k, len(nums))):
        largest_elements.append((- heapq.heappop(max_heap)))
    return sorted(largest_elements, reverse=True)
