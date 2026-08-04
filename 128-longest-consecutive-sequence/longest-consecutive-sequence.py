class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        count = 0
        for n in num_set:
            if n + 1 not in num_set:
                curr = n
                curr_count = 0
                while curr in num_set:
                    curr_count += 1
                    curr -= 1
                count = max(count, curr_count)
        return count
