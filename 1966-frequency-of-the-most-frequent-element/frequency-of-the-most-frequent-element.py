class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        '''
        sort
        rule out biggest element 
        two pointers
        elements are closest to each other
        make element next to each other equal

        
        '''
        l = 0
        max_frequency, total = 0, 0
        nums.sort()
        for r in range(len(nums)):
            total += nums[r]
            while (r - l + 1) * nums[r] > total + k and l < r:
                total -= nums[l]
                l += 1
            max_frequency = max(max_frequency, r - l + 1)

            
        return max_frequency