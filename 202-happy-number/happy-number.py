class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            if n in seen:
                return False # cycle
            seen.add(n)
            # calc sum of squares of digits
            total = 0
            for num in str(n):
                total += int(num) ** 2
            n = total
        return True