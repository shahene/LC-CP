class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # xor 
        bitmask = 0
        for n in nums:
            bitmask ^= n
        return bitmask
