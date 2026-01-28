class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        brute force --> O(n^3)
        O(n) palindromic checking * O(n^2) checking every single substring in s

        key: palindromic checking from middle + expanding outward
        caveat: even length palindromes, set l = i & r = i + 1
                effectively checks two characters at a time and not 1 in beginning
        optimized --> O(n^2)
        O(n) processing * O(n) palindromic checking

        Auxiliary Space (not counting input or output) --> O(1)
        '''
        res_length = 0
        res = ''
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[r] == s[l]:
                # odd length
                if (r - l + 1) > res_length:
                    res_length = r - l + 1
                    res = s[l: r + 1]
                l -= 1
                r += 1
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[r] == s[l]:
                # even length
                if (r - l + 1) > res_length:
                    res_length = r - l + 1
                    res = s[l: r + 1]
                l -= 1
                r += 1
        return res