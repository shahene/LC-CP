class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        '''
        sliding window
        reach >= target
        subtract from the beginning of the array
        move indices 
        keep track of length
        O(n) time + O(1) space
        '''
        l = running_sum = 0
        min_length = math.inf
        for r in range(len(nums)):
            running_sum += nums[r]
            while running_sum >= target and l <= r:
                min_length = min(min_length, r - l + 1)
                running_sum -= nums[l]
                l += 1
        return min_length if min_length != math.inf else 0