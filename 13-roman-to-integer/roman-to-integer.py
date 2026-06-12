class Solution:
    def romanToInt(self, s: str) -> int:
        roman_int_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        for i in range(1, len(s)):
            prev_roman_int, cur_roman_int = roman_int_map[s[i-1]], roman_int_map[s[i]]
            if prev_roman_int < cur_roman_int:
                total -= prev_roman_int
            else:
                total += prev_roman_int
                print(total)
        final_roman_int = roman_int_map[s[-1]]
        total += final_roman_int
        return total