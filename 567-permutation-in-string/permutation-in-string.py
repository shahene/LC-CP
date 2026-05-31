class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = collections.Counter(s1)
        s1_length = len(s1)
        l = 0
        counter = 0
        s2_map = {}
        for r in range(len(s2)):
            if s2[r] not in s2_map:
                s2_map[s2[r]] = 0
            s2_map[s2[r]] += 1
            if r - l + 1 == s1_length:
                if s2_map == s1_map: return True
                s2_map[s2[l]] -= 1
                if s2_map[s2[l]] == 0: del s2_map[s2[l]]
                l += 1
        print(s2_map, s1_map)
        return False