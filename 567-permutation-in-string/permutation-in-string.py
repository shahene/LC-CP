class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        orig_map = collections.Counter(s1)
        l = 0
        n_map = {}
        for r in range(len(s2)):
            if s2[r] not in n_map:
                n_map[s2[r]] = 0
            n_map[s2[r]] += 1
            print(n_map)
            if r >= len(s1) - 1:
                if n_map == orig_map:
                    return True
                n_map[s2[l]] -= 1
                if n_map[s2[l]] == 0:
                    del n_map[s2[l]]
                l += 1
        return False