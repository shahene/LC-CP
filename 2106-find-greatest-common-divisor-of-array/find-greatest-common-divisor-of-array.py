class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_, max_ = min(nums), max(nums)
        max_divisor = 1
        for i in range(1, min_ + 1):
            if max_ % i == 0 and min_ % i == 0:
                max_divisor = i
        return max_divisor
