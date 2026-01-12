class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        outer loop to iterate through array, fix nums[i]
        if i != 0 and nums[i] == nums[i-1]: continue
        nums[i] + nums[j] + nums[k] == 0
        looking for above
        if < 0, increment l
        if > 0, decrement r
        if total == 0:
            increment l while nums[l] == nums[l-1] and l < len(nums)
        
        O(n^2) time + O(1) space
        '''
        output = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]: continue
            j, k = i + 1, len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    output.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < len(nums) and nums[j] == nums[j-1]:
                        j += 1
        return output