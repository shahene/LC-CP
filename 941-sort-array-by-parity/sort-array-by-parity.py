class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        '''
        nums = [3, 1, 2, 4]
        nums = [4, 1, 2, 3]
        nums = [4, 1, 2, 3]
        nums = [4, 2, 1, 3]
        '''
        left, right = 0, len(nums) - 1
        index = 0
        while index < right:
            if nums[index] & 1 == 0:
                left += 1
                index += 1
            else:
                nums[index], nums[right] = nums[right], nums[index]
                right -= 1
        return nums
