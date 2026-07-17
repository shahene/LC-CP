class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l, tot_sum, running_sum = 0, -math.inf, 0
        for r in range(len(nums)):
            right_num = nums[r]
            running_sum += nums[r]
            tot_sum = max(tot_sum, running_sum)
            while running_sum < 0 and l <= r:
                running_sum -= nums[l]
                l += 1
        return tot_sum
