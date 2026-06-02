class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        fixed_arr = [0] * 26
        for s_char, t_char in zip(s, t):
            fixed_arr[ord(s_char) - ord('a')] += 1
            fixed_arr[ord(t_char) - ord('a')] -= 1
        for check in fixed_arr:
            if check != 0: return False
        return True