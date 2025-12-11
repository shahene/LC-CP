class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_consecutive = 0
        for n in num_set:
            if n - 1 not in num_set:
                length = 0
                while n + length in num_set:
                    length += 1
                max_consecutive = max(max_consecutive, length)
        return max_consecutive