class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        count = 0
        # must consist of only vowels
        for start in range(len(word)):
            seen = set()
            for end in range(start, len(word)):
                if word[end] not in vowels:
                    break
                
                seen.add(word[end])
                if len(seen) == 5:
                    count += 1
        return count

            