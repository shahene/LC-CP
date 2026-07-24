class Solution:
    def reverseBits(self, n: int) -> int:
        '''
        1111 0000
        0000 1111
        '''
        bits_int = [0] * 32
        index = 0
        while index != 32:
            bits_int[index] = str((n & 1))
            n >>= 1
            index += 1
        bit = '0b' + ''.join(bits_int)
        return int(bit, 2)