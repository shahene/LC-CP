class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        char_ordering = [0] * 26
        for n in s:
            index = ord(n) - ord('a')
            char_ordering[index] += 1
        for n in t:
            index = ord(n) - ord('a')
            if char_ordering[index] == 0: return False
            char_ordering[index] -= 1
            if char_ordering[index] < 0: return False
        return True
