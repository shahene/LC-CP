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
        num_set = set(nums)
        max_length = 0
        for n in num_set:
            if n - 1 not in num_set:
                length = 0
                while n + length in num_set:
                    length += 1
                max_length = max(max_length , length)
        return max_length
