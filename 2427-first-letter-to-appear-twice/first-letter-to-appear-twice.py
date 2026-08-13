class Solution:
    def repeatedCharacter(self, s: str) -> str:
        letter_set = set()
        for n in s:
            if n in letter_set:
                return n
            letter_set.add(n)