class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''
        find longest common prefix amongst an array of strings
        if there is no common prefix, return an empty string
        
        iterate through first word, look at first letter make sure it is the same for all 
        other words, else return lcp
        if it is 
        lcp += valid character
        
        '''
        lcp = ''
        first_word = strs[0]
        i = 0
        for first_word_char in first_word:
            for n in strs:
                print(type(n))
                if i >= len(n) or n[i] != first_word_char:
                    return lcp
            lcp += first_word_char
            i += 1
        return lcp
        
        return lcp