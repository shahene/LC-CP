class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        n objects colored red, white or blue
        sort them in place
        so that objects of the same color are adjacent

        0, 1, 2 -> in that order

        ok so we can have two pointers
        l, r 
        whenever we see a 0, we insert 0 into nums[l], increment l (increment i)
        whenever we see a 2, we insert 2 into nums[r], decrement r but don't increment i
        whenever we see 1, just skip (increment i) 

        our main condition will be while i < r
        this will be in-place so O(n) time + O(1) space
        '''
        l, r = 0, len(nums) - 1
        index = 0
        while index <= r:
            val = nums[index]
            if val == 0:
                nums[index], nums[l] = nums[l], nums[index]
                l += 1
                index += 1
            elif val == 1:
                index += 1
            else:
                nums[index], nums[r] = nums[r], nums[index]
                r -= 1
