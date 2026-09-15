class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        count_chars = collections.defaultdict(int)
        count_max = 0
        for r in range(len(s)):
            current_char = s[r]
            count_chars[current_char] += 1
            while count_chars[current_char] > 1:
                left_char = s[l]
                count_chars[left_char] -= 1
                l += 1
            count_max = max(count_max, r - l + 1)
        return count_max