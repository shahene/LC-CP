class Solution:
    def bitwiseComplement(self, n: int) -> int:
        temp = n
        bitwise_mask = 0
        if n == 0: return 1
        while temp != 0:
            bitwise_mask <<= 1
            bitwise_mask |= 1
            temp >>= 1
        return n ^ bitwise_mask