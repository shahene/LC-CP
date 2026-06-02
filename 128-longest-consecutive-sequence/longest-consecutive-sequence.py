class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_count = 0
        for n in num_set:
            running_count = 0
            if (n + 1) not in num_set:
                while n in num_set:
                    running_count += 1
                    n -= 1
                max_count = max(max_count, running_count)
        return max_count
