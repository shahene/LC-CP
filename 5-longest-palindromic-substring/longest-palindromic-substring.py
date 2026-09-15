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
        n = len(s)
        longest = ''
        def expand(l, r):
            while l in range(n) and r in range(n) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1: r]

        for i in range(n):
            odd_palindrome = expand(i, i)
            even_palindrome = expand(i, i + 1)
            if len(odd_palindrome) > len(longest):
                longest = odd_palindrome
            if len(even_palindrome) > len(longest):
                longest = even_palindrome
        return longest


            