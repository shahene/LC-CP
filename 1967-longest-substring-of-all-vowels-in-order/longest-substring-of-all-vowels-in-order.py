class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        '''
        each of five vowels appears at least once
        vowel letters must be sorted in alphabetical order

        how to determine if a substring is beautiful?
        so only 5 vowel letters
        a e i o u
        in beginning we are looking for a, whenever we find next vowel
        we are looking for next vowel. if mismatch non beautiful.
        move pointer up to current position
        otherwise keep moving up until we have all 5 vowels present
        ['u', 'o', 'i', 'e', 'a']
        look at last index of vowel array
        when mismatch restart
        move pointers up
        if we find a pop from a keep going while 
        whenever mismatch
        reset local counter to 0
        while a string is valid and beautiful:
            keep increasing local counter and incresing global counter 
            when string is invalid : break
        
        restart
        how to find longest beautiful substring
        '''
        l = r = 0
        prev_vowel = word[l]
        vowels = {
            'a': 'e',
            'e': 'i',
            'i': 'o',
            'o': 'u',
            'u': 'b'
        }
        local_count = 0
        max_count = 0
        while r < len(word):
            current_vowel = word[r]
            if current_vowel != prev_vowel and current_vowel != vowels[prev_vowel]:
                local_count = 0
                l = r
            elif current_vowel == vowels[prev_vowel]:
                local_count += 1

            if local_count == 4: max_count = max(max_count, r - l + 1)
            prev_vowel = current_vowel
            r += 1
        return max_count


            

