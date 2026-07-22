class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        beg, end = 0, len(nums) - 1
        # how to find parity of number?
        # use
        while beg < end:
            if nums[beg] & 1 == 1:
                tmp = nums[end]
                nums[end] = nums[beg]
                nums[beg] = tmp
                end -= 1
            else:
                beg += 1
        return nums