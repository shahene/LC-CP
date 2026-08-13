class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_count = 0
        left_pointer = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[left_pointer], nums[r] = nums[r], nums[left_pointer]
                left_pointer += 1
