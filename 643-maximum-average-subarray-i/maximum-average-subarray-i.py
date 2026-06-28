class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg_val = -math.inf
        l = 0
        running_sum = 0
        for r in range(len(nums)):
            running_sum += nums[r]
            if r >= k - 1:
                max_avg_val = max(max_avg_val, running_sum / (r - l + 1))
                running_sum -= nums[l]
                l += 1
        return max_avg_val