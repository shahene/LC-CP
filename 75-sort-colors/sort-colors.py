class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        l, r = 0, len(nums) - 1

        while l < r and index <= r:
            if nums[index] == 0:
                nums[l], nums[index] = nums[index], nums[l]
                l += 1
                index += 1
            elif nums[index] == 2:
                nums[r], nums[index] = nums[index], nums[r]
                r -= 1
            else:
                index += 1