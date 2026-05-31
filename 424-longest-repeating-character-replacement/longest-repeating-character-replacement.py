class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        # choose any character + k replacements -> 
        '''
        sliding window of some kind
        hashmap -- keeps track of number characters in window -- use it to get max_count
        (r - l + 1) - max_count > k ==> invalid
        if invalid:
            from left start sliding -- l += 1
        if valid:
            record max length
        '''
        map_characters = {}
        l = 0
        max_char = 0
        for r in range(len(s)):
            if s[r] not in map_characters:
                map_characters[s[r]] = 0
            map_characters[s[r]] += 1 
            max_char = max(max_char, map_characters[s[r]])
            while ((r - l + 1) - max_char) > k:
                map_characters[s[l]] -= 1
                l += 1
            
            max_length = max(max_length, r - l + 1)
        return max_length