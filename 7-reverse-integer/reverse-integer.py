class Solution:
    def reverse(self, x: int) -> int:
        total = 0
        negative_flag = x < 0
        x = abs(x)
        def recursive_reverse(n, total):
            if n == 0: return total
            total = (total * 10) + (n % 10)
            return recursive_reverse(n // 10, total)
        tot = recursive_reverse(x, total)
        if tot >= -2 ** 31 and tot <= (2 ** 31) - 1:
            return tot if not negative_flag else -tot
        else:
            return 0
        