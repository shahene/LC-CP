class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        int_digits = int(''.join(str(num) for num in digits))
        int_digits += 1
        string_digits = str(int_digits)
        string_digit_arr = [int(s) for s in string_digits]
        return string_digit_arr