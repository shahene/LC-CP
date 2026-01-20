class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        given a string s and an integer k
        choose any character of the string and change it to any other uppercase 
        English character
        can perform this operation at most k times
        return length of longest string containing the same letter you can get after
        performing the above operations

        s = "ABAB", k = 2
        SOLUTION:
        greedy + sliding window approach
        keep track of max repeating letter using frequency map
        (r - l + 1) - max_repeating_letter
        => returns all the remaining letters, which we can change if <= k
        while above operation > k:
            move left pointer up & subtract from frequency until condition does not hold
        return max window that is valid
        O(n) time -> only go through string once
        O(n) space -> worst case for frequency map
        '''
        l, max_repeating_letter, max_window, frequency_map = 0, 0, 0, {}
        for r in range(len(s)):
            cur_char = s[r]
            if cur_char not in frequency_map:
                frequency_map[cur_char] = 0
            frequency_map[cur_char] += 1
            max_repeating_letter = max(max_repeating_letter, frequency_map[cur_char])
            while (r - l + 1) - max_repeating_letter > k and l < len(s):
                left_char = s[l]
                frequency_map[left_char] -= 1
                if frequency_map[left_char] == 0:
                    del frequency_map[left_char]
                l += 1
            max_window = max(max_window, r - l + 1)
        return max_window
