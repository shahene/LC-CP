class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        s_sorted = sorted(s)
        t_sorted = sorted(t)
        index = 0
        while index < len(s):
            if s_sorted[index] != t_sorted[index]:
                return False
            index += 1
        return True
        