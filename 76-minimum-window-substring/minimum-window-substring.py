class Solution:
    def minWindow(self, s: str, t: str) -> str:
        substr_start, minLength = 0, math.inf
        t_counter = collections.Counter(t)
        matchings = 0
        l = 0
        for r in range(len(s)):
            cur_char = s[r]
            if cur_char in t_counter:
                t_counter[cur_char] -= 1
                if t_counter[cur_char] >= 0:
                    matchings += 1
                
            while matchings == len(t):
                if minLength > r - l + 1:
                    minLength = r - l + 1
                    substr_start = l
                left_char = s[l]
                l += 1
                if left_char in t_counter:
                    if t_counter[left_char] == 0:
                        matchings -= 1
                    t_counter[left_char] += 1
                

        return '' if minLength == math.inf else s[substr_start: substr_start + minLength]