class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        max_ones = 0
        v = k
        for r in range(len(nums)):
            if nums[r] == 0:
                v -= 1
            while v < 0:
                if nums[l] == 0:
                    v += 1
                l += 1
            max_ones = max(max_ones, r - l + 1)
        return max_ones 