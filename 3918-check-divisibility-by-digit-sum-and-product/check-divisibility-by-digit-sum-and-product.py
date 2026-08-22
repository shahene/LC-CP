class Solution:
    def checkDivisibility(self, n: int) -> bool:
        # find digit sum and product of digit
        su, pro = self.digit_sum(n), self.product_digit(n)
        return n % (su + pro) == 0
    def digit_sum(self, n):
        if n == 0:
            return n
        return (n % 10) + self.digit_sum(n // 10)
    def product_digit(self, n):
        if n < 10:
            return n

        return (n % 10) * self.product_digit(n // 10)