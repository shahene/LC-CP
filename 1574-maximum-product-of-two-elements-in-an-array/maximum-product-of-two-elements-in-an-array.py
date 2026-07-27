class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        f_biggest, s_biggest = -math.inf, -math.inf
        for i, n in enumerate(nums):
            if n > f_biggest:
                f_biggest, s_biggest = n, f_biggest
            elif n > s_biggest:
                s_biggest = n
        return (f_biggest - 1) * (s_biggest - 1)