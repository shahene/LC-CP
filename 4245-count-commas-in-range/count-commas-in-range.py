class Solution:
    def countCommas(self, n: int) -> int:
        '''
        numbers in range 1 => 10^5 have 1 comma
        (1002 - 1000) + 1
        (10000 - 1000) + 1 => 1055
        '''
        if n < 1000: return 0
        return (n - 1000) + 1
