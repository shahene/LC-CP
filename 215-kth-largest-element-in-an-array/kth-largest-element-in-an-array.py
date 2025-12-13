import heapq
# heapq.heapify_max(list)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-1 * n for n in nums]
        heapq.heapify(nums)
        n = math.inf
        for _ in range(k):
            n = heapq.heappop(nums)
        return n * -1
