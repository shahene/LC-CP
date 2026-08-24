class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        '''
        given integer array nums
        alternating sum of nums is value
        by adding at even indices and subtrating at odd indices
        '''
        res = 0
        for i, n in enumerate(nums):
            if i & 1 == 0:
                res += n
            else:
                res -= n
        return res