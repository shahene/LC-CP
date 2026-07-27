class Solution:
    def maxProduct(self, n: int) -> int:
        max_digit_one, max_digit_two = -math.inf, -math.inf
        while n:
            digit = n % 10
            n //= 10
            if digit > max_digit_one:
                max_digit_one, max_digit_two = digit, max_digit_one
            elif digit > max_digit_two:
                max_digit_two = digit
        return max_digit_one * max_digit_two
