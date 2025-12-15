import heapq
# heapq.heapify_max(list)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = [-1 * n for n in nums]
        heapq.heapify(min_heap)
        n = math.inf
        for _ in range(k):
            n = heapq.heappop(min_heap)
        return -1 * n
