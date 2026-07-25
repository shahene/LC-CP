class Solution:
    def reverseBits(self, n: int) -> int:
        '''
        input: integer n
        output: integer n after bits have been reversed

        bit = (n & 1)

        n|= bit << (31 - 1)
        10101010101010101
        10000000000000000
        10101010110101010

        n = 4, 100, 001 => return 1

        '''
        res = 0
        for i in range(32):
            bit = ((n >> i) & 1)
            res |= (bit << (31 - i))
        return res