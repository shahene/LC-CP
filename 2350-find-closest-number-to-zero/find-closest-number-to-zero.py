class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest_num = abs(nums[0])
        actual = nums[0]
        for i in range(1, len(nums)):
            if abs(nums[i]) < closest_num:
                closest_num = abs(nums[i])
                actual = nums[i]
            if abs(nums[i]) == closest_num and nums[i] > actual:
                actual = nums[i]
        return actual
