class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        given two strings s and t of lengths m and n respectively
        
        input: string s and pattern t
        output: minimum window substring which contains all characters of t

        edge cases: len(t) > len(s)
                    given one letter for both s and t (same letter)
        
        
        Input: s = "ADOBECODEBANC", t = "ABC"

        match: sliding window

        count of t map => {
            "A": 1,
            "B": 1,
            "C": 1
        }

        substr_start = 0
        window_length = math.inf
        matched = 0 (to count matching of characters)

        while number of characters matched:
            start decreasing the size of the window by sliding the window


        SOL:
        We will keep a running count of every matching instance of a character.
        Whenever we have matched all the characters, we will try to shrink the window from the beginning, keeping track of the smallest substring that has all the matching characters.
        We will stop the shrinking process as soon as we remove a matched character from the sliding window. One thing to note here is that we could have redundant matching characters, e.g., we might have two ‘a’ in the sliding window when we only need one ‘a’. In that case, when we encounter the first ‘a’, we will simply shrink the window without decrementing the matched count. We will decrement the matched count when the second ‘a’ goes out of the window.
        '''
        t_count_map = collections.Counter(t)
        l, matched, window_length = 0, 0, math.inf
        substr_start = 0
        # n_characters_needed = sum(t_count_map.values()) # DONT NEED THIS: LEN(T) HAS NUMBER OF CHARACTERS THAT WE NEED
        for r in range(len(s)):
            char = s[r]
            if char in t_count_map:
                t_count_map[char] -= 1
                if t_count_map[char] >= 0:
                    matched += 1
            while matched == len(t):
                l_char = s[l]
                if r - l + 1 < window_length:
                    window_length = r - l + 1
                    substr_start = l
                if l_char in t_count_map:
                    if t_count_map[l_char] == 0:
                        matched -= 1
                    t_count_map[l_char] += 1
                l += 1
                
        return "" if window_length == math.inf else s[substr_start: substr_start + window_length]
        