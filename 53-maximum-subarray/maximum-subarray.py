class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        tot_max = -math.inf
        running_sum, l = 0, 0
        for r in range(len(nums)):
            running_sum += nums[r]
            tot_max = max(tot_max, running_sum)
            while running_sum < 0 and l <= r:
                running_sum -= nums[l]
                l += 1
            
        return tot_max
            
