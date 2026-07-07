class Solution:
    def sumAndMultiply(self, n: int) -> int:
        total = 0
        arr_non_zero = collections.deque([])
        while n:
            nonzero = n % 10
            total += nonzero
            n = n // 10
            if nonzero != 0:
                arr_non_zero.appendleft(str(nonzero))
        digits = ''.join(arr_non_zero)
        if not digits: return 0
        return int(digits) * total
        
        
