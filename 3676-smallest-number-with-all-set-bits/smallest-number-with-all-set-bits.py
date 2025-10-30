class Solution:
    def smallestNumber(self, n: int) -> int:
        '''
        given positive number n
        return smallest number x greater than or equal to n
        1 -> 0
        11 -> 3
        111 -> 7
        '''
        i = 1
        for _ in range(n):
            if i >= n:
                return i
            else:
                i = 2 * i + 1