class Solution:
    def hammingWeight(self, n: int) -> int:
        '''
        given a positive integer n, write a function that returns the number of set bits in its binary 
        representation

        (also known as the Hamming weight)
        while x:
            count_bits += (x & 1)
            right shift to move to next bit >>
        return count_bits
        O(N) where N is the number of bits in binary rep. of n
        O(1) space
        '''
        count_bits = 0
        while n:
            count_bits += (n & 1)
            n >>= 1
        return count_bits
