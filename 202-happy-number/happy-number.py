class Solution:
    def isHappy(self, n: int) -> bool:
        def number_sum(s):
            total = 0
            while s:
                digit = s % 10
                total += (digit ** 2)
                s //= 10
            return total
        slow, fast = number_sum(n), number_sum(number_sum(n))
        while slow != fast and slow != 1:
            slow = number_sum(slow)
            fast = number_sum(number_sum(fast))
        
        return slow == 1