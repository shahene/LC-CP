class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length, max_repeat_letter, l = 0, 0, 0
        frequency_map = {}
        for r in range(len(s)):
            cur_char = s[r]
            if cur_char not in frequency_map:
                frequency_map[cur_char] = 0
            frequency_map[cur_char] += 1
            max_repeat_letter = max(max_repeat_letter, frequency_map[cur_char])
            while (r - l + 1 - max_repeat_letter > k):
                left_char = s[l]
                frequency_map[left_char] -= 1
                l += 1
            
            max_length = max(max_length, r - l + 1)

        return max_length