class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        treat each character as middle
        expand outward 
        keep track of starting_index and ending_index
        check odd and even length strings
        '''
        starting_longest, ending_longest = -1, -1
        max_length = 0
        for i in range(len(s)):
            # odd
            current_length = 1
            left_char, right_char = i - 1, i + 1
            while left_char in range(len(s)) and right_char in range(len(s)) and s[left_char] == s[right_char]:
                left_char -= 1
                right_char += 1
                current_length += 2
            if current_length > max_length:
                starting_longest = left_char + 1
                ending_longest = right_char
                max_length = current_length
            # even
            current_length = 0
            left_char, right_char = i, i + 1
            while left_char in range(len(s)) and right_char in range(len(s)) and s[left_char] == s[right_char]:
                left_char -= 1
                right_char += 1
                current_length += 2
            if current_length > max_length:
                starting_longest = left_char + 1
                ending_longest = right_char
                max_length = current_length
        if starting_longest == -1: return ''
        return s[starting_longest: ending_longest]


            