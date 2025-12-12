class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums) - 1
        index = 0
        while index <= r:
            if nums[index] == 0:
                nums[l], nums[index] = nums[index], nums[l]
                l += 1
                index += 1
            elif nums[index] == 1:
                index += 1
                continue
            else:
                nums[index], nums[r] = nums[r], nums[index]
                r -= 1

