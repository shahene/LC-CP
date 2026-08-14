class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        l = 0
        max_length = 0
        character_map = collections.defaultdict(int)
        for r, n in enumerate(s):
            character_map[n] += 1
            while l < r and character_map[n] > 2:
                left_char = s[l]
                character_map[left_char] -= 1
                l += 1
            max_length = max(max_length, r - l + 1)
        return max_length