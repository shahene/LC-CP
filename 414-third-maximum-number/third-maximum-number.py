class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        '''
        O(3n), find max1 max2 max3
        '''
        max1, max2, max3 = max(nums), float('-inf'), float('-inf')
        if len(nums) < 3: return max1
        for i in range(len(nums)):
            if nums[i] != max1 and nums[i] > max2:
                max2 = nums[i]
        for i in range(len(nums)):
            if nums[i] != max2 and nums[i] != max1 and nums[i] > max3:
                max3 = nums[i]
        print(max1, max2, max3)
        return max3 if max3 != float('-inf') else max1
