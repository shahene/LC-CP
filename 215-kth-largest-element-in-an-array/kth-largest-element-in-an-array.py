class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        nums = [-1 * n for n in nums]
        heapq.heapify(nums)
        max_num = -1
        for _ in range(k):
            n = -1 * heapq.heappop(nums)            
        return n