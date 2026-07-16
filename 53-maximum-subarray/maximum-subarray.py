class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -math.inf
        l = 0
        running = 0
        for i in range(len(nums)):
            while running < 0 and l <= i:
                running -= nums[l]
                l += 1
                
            running += nums[i]
            max_sum = max(max_sum, running)
        return max_sum