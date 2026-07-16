class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map, t_map = collections.Counter(s), collections.Counter(t)
        return s_map == t_map