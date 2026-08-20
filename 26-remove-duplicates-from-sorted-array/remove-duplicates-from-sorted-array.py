class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        input: list of nums
        output: integer representing the number of unique elements k

        unique_ptr = 0
        index = 0
        while index < len(nums):
            if index == 0 or nums[index] != nums[unique_ptr - 1]:
                nums[unique_ptr] = nums[index]
                index += 1
                unique_ptr += 1
            else:
                index += 1
        return unique_ptr + 1
        '''
        unique_ptr = 0
        index = 0
        while index < len(nums):
            if index == 0 or nums[index] != nums[unique_ptr - 1]:
                nums[unique_ptr] = nums[index]
                index += 1
                unique_ptr += 1
            else:
                index += 1
        return unique_ptr