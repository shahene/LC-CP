class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max_repeat_letter, count_letters = 0, {}
        for r in range(len(s)):
            if s[r] not in count_letters:
                count_letters[s[r]] = 0
            count_letters[s[r]] += 1
            while count_letters[s[r]] > 1:
                count_letters[s[l]] -= 1
                l += 1
            max_repeat_letter = max(max_repeat_letter, r - l + 1)
        return max_repeat_letter