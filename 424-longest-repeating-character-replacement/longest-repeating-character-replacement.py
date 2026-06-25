class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        validity condition: if (current_window - max_repeating_letter) > k
        
        while window is invalid:
            slide window from left (shrinks window size which would eventually make window valid
            if that is possible)
                decrement frequency 

            what happens to max repeating letter?
                well assuming we already recorded window size earlier (we don't need to update it)
                because if we don't find a larger max repeating letter count in the future, we will not have a larger substring (so doesn't matter)
        
        O(N) time + O(N) space -- worst case k == length of s (all different characters)
        
        edge cases: lower case letters, empty string (must return 0 by default), k > len(s)
        '''
        freq_map = collections.defaultdict(int)
        l, max_length = 0, 0
        max_repeating_letter = 0
        for r, n in enumerate(s):
            freq_map[n] += 1
            max_repeating_letter = max(max_repeating_letter, freq_map[n])
            while (r - l + 1) - max_repeating_letter > k:
                left_char = s[l]
                freq_map[left_char] -= 1
                l += 1
            max_length = max(max_length, r - l + 1)
        return max_length


