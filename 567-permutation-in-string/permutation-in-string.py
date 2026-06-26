class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        s1 = "ab"
        s2 = "eidbaooo"

        s1_frequency_map = {
            "a": 1,
            "b": 1
        }


        
        if len(s1) > len(s2): return False
        
        s2_frequency_map = {}
        sliding window
        l = 0
        iterate through s2 with r 
            add each character to s2 frequency w relevant frequency
        once we reach length k (k = len(s1)):
            if s2_frequency_map == s1_frequency_map: return True
                look at character at l 
                decrement frequency
                if s2_frequency_map[char at l] == 0 del from map
                l += 1
        
        return False

        '''
        if len(s1) > len(s2): return False
        l = 0

        s1_frequency_map = collections.Counter(s1)
        s2_frequency_map = collections.defaultdict(int)

        for r in range(len(s2)):
            current_char = s2[r]
            s2_frequency_map[current_char] += 1

            window = r - l + 1
            if window >= len(s1):
                if s2_frequency_map == s1_frequency_map: return True
                left_character = s2[l]
                s2_frequency_map[left_character] -= 1
                if s2_frequency_map[left_character] == 0: del s2_frequency_map[left_character]
                l += 1
                
        return False