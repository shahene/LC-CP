import heapq
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        min_heap = [-1 * int(n) for n in nums]
        heapq.heapify(min_heap)
        n = 0
        for _ in range(k):
            n = heapq.heappop(min_heap)
        return str(-1 * n)