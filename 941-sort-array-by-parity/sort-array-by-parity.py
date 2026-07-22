class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        beg, end = 0, len(nums) - 1
        # how to find parity of number?
        # use
        for n in nums:
            if n & 1 == 0:
                res[beg] = n
                beg += 1
            else:
                res[end] = n
                end -= 1
        return res