class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # if n == 0
        if n < 0: n &= (n - 1)
        return n & (n - 1) == 0 and n != 0