from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        counter_s, counter_t = defaultdict(int), defaultdict(int)
        for char1, char2 in zip(s, t):
            counter_s[char1] += 1
            counter_t[char2] += 1
        return counter_s == counter_t

        