class Solution:
    def isPalindrome(self, s: str) -> bool:
        formatted_arr = []
        for n in s: 
            if n.isalnum(): formatted_arr.append(n.lower())
        l, r = 0, len(formatted_arr) - 1
        while l <= r:
            if formatted_arr[l] != formatted_arr[r]: return False
            l += 1
            r -= 1
        return True