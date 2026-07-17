class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        def set_bits(n):
            num_bits = 0
            while n:
                num_bits += n & 1
                n >>= 1
            return num_bits
        total = 0
        for i in range(len(nums)):
            num_b = set_bits(i)
            if k == num_b:
                total += nums[i]
        return total

        