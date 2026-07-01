class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        '''
        number ^= new number
        logs previous bits

        so for example 1 or 3
        001 ^ 011 = 1
        0011 ^ 1000 = 001011
        001011 ^ 110000 = 111011
        111011 and 001010 != 0

        '''
        res = 0
        cur = 0
        l = 0
        for r in range(len(nums)):
            while cur & nums[r] and l <= r:
                cur ^= nums[l]
                l += 1
            cur |= nums[r]
            res = max(res, r - l + 1)
        return res

        