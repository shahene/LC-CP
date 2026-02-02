class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        Input: nums = [5,4,-1,7,8]
        Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
        '''
        l, running_sum = 0, nums[0]
        maximum_sum = running_sum
        for i in range(1, len(nums)):
            while l < i and running_sum < 0:
                running_sum -= nums[l]
                l += 1 
            running_sum += nums[i]
            maximum_sum = max(running_sum, maximum_sum)
        return maximum_sum