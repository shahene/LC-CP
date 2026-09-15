class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        pretend that each character is middle
        check left and right if they are palindromes
        goes down to O(n^2)
        for even length palindrome edge case:
            set l to i and r to i + 1
            and expand with two chars instead of 1 (like in odd length)
        '''
        res_length, starting_substr, ending_substr = 0, 0, 0
        for i in range(len(s)):
            l, r = i, i
            while l in range(len(s)) and r in range(len(s)) and s[l] == s[r]:
                if (r - l + 1) > res_length:
                    starting_substr = l
                    ending_substr = r
                    res_length = r - l + 1
                l -= 1
                r += 1
            l, r = i, i + 1
            while l in range(len(s)) and r in range(len(s)) and s[l] == s[r]:
                if (r - l + 1) > res_length:
                    starting_substr = l
                    ending_substr = r
                    res_length = r - l + 1
                l -= 1
                r += 1
        return s[starting_substr: ending_substr + 1]

            