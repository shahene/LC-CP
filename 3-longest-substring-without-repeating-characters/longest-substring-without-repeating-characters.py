class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        sliding window
        keep hashmap -- count of characters
        if count exceeds 1 for any character, duplicate found
        then we must delete character from the left, decrementing count as we go
        until that character's count is 1 or less
        keep track of length as you go
        O(n) time + O(n) space 
        '''
        count_hashmap = {}
        max_length = 0
        l = 0
        for r in range(len(s)):
            current_char = s[r]
            if current_char not in count_hashmap:
                count_hashmap[current_char] = 0
            count_hashmap[current_char] += 1
            while count_hashmap[current_char] > 1:
                left_char = s[l]
                count_hashmap[left_char] -= 1
                l += 1
            max_length = max(max_length, r - l + 1)
        return max_length
