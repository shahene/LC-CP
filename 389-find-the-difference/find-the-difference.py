class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_count, t_count = collections.Counter(s), collections.Counter(t)
        for n in t:
            if n not in s or s_count[n] != t_count[n]: return n