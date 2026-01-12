class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        100-> 101
        4-> 3
        200-> 199
        1-> 0
        3-> 2
        2-> 1
        '''
        num_map = {}
        max_length = 0
        for n in nums:
            num_map[n] = n + 1
        for n in num_map:
            if num_map[n] not in num_map:
                length = 0
                while n - length in num_map:
                    length += 1
                max_length = max(max_length, length)
        return max_length
        