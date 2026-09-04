class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        for i in range(len(nums)):
            maximum = max(nums[0: i + 1])
            minimum = min(nums[i: n])
            if maximum - minimum <= k: return i
        return -1