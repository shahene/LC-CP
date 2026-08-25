class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        if x == 0: return True
        reversed_x = self.reverse_number(x)
        return x == self.reverse_number(x)
    def reverse_number(self, n):
        digits = int(math.log10(n)) + 1
        return self.helper(n, digits)
    def helper(self, n, digits):
        if n % 10 == n: return n
        rem = n % 10
        return rem * (10**(digits - 1)) + self.helper(n // 10, digits - 1)
