class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        given an unsorted array of integers nums, 
        return the lenth of the longest consecutive elements sequence

        nums = [100, 4, 200, 1, 3, 2]
        100
        4
        200
        1
        3
        2
        create set
        iterate through set, not original array (don't want to add extra steps here if we have duplicates)
        if current element + 1 does not exist, this is the end and we start counting longest sequence
        '''
        num_set = set(nums)
        max_length = 0
        for n in num_set:
            length = 0
            if n + 1 not in num_set:
                while n - length in num_set:
                    print(n - length)
                    length += 1
            max_length = max(max_length, length)
        return max_length