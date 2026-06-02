class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        fixed_arr = [0] * 26
        for s_char in s:
            fixed_arr[ord(s_char) - ord('a')] += 1
        for t_char in t:
            fixed_arr[ord(t_char) - ord('a')] -= 1
        for check in fixed_arr:
            if check != 0: return False
        return True