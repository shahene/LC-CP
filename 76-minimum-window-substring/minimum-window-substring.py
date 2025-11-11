class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_pattern = collections.Counter(t)
        substr_start, min_length, window_start, matched = 0, len(s) + 1, 0, 0
        for window_end in range(len(s)):
            right_char = s[window_end]
            if right_char in t_pattern:
                t_pattern[right_char] -= 1
                if t_pattern[right_char] >= 0:
                    matched += 1
            
            while matched == len(t):
                left_char = s[window_start]
                if window_end - window_start + 1 < min_length:
                    min_length = window_end - window_start + 1
                    substr_start = window_start
                if left_char in t_pattern:
                    if t_pattern[left_char] == 0:
                        matched -= 1
                    t_pattern[left_char] += 1
                window_start += 1

        if min_length < len(s) + 1:
            return s[substr_start: substr_start + min_length]
        else:
            return ''
        