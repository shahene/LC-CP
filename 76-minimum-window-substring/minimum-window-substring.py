class Solution:
    def minWindow(self, s: str, t: str) -> str:
        matched, substr_start, t_frequency_map, substr_max, l = 0, 0, collections.Counter(t), math.inf, 0
        for r in range(len(s)):
            current_char = s[r]
            if current_char in t_frequency_map:
                t_frequency_map[current_char] -= 1
                if t_frequency_map[current_char] >= 0:
                    matched += 1
            while matched == len(t) and l <= r:
                if r - l + 1 < substr_max:
                    substr_max = r - l + 1
                    substr_start = l
                
                char = s[l]
                l += 1
                if char in t_frequency_map:
                    if t_frequency_map[char] == 0:
                        matched -= 1
                    t_frequency_map[char] += 1
                
        
        return "" if substr_max == math.inf else s[substr_start: substr_start + substr_max]