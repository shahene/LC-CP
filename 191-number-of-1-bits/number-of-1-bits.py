class Solution:
    def hammingWeight(self, n: int) -> int:
        bitmask, count = 1, 0
        while n:
            count += 1
            n &= n - 1
        return count