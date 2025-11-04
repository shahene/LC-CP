class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter = collections.Counter(s1)
        window_start, matched = 0, 0
        for window_end in range(len(s2)):
            right_char = s2[window_end]
            if right_char in s1_counter:
                s1_counter[right_char] -= 1
                if s1_counter[right_char] == 0:
                    matched += 1
            if matched == len(s1_counter):
                return True
            if window_end - window_start + 1 >= len(s1):
                left_char = s2[window_start]
                if left_char in s1_counter:
                    if s1_counter[left_char] == 0:
                        matched -= 1
                    s1_counter[left_char] += 1
                window_start += 1
            
        
                    
        return False