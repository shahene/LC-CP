class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        
        '''
        substr_start, l, t_counter, window_length = 0, 0, collections.Counter(t), math.inf
        matched = 0
        if len(t) > len(s): return ""
        
        for r in range(len(s)):
            char = s[r]
            if char in t_counter:
                t_counter[char] -= 1
                if t_counter[char] >= 0:
                    matched += 1
            
            while matched == len(t):
                if r - l + 1 < window_length:
                    window_length = r - l + 1
                    substr_start = l
                left_char = s[l]
                if left_char in t_counter:
                    if t_counter[left_char] == 0:
                        matched -= 1
                    t_counter[left_char] += 1
                
                l += 1
                
                        


        return "" if window_length == math.inf else s[substr_start: substr_start + window_length]