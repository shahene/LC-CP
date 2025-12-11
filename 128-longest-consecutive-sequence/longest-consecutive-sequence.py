class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        cur_consecutive, max_consecutive = 1, 1
        for i in range(1, len(nums)):
            if nums[i - 1] + 1 == nums[i]:
                cur_consecutive += 1
            elif nums[i-1] == nums[i]:
                continue
            else:
                cur_consecutive = 1
            max_consecutive = max(max_consecutive, cur_consecutive)
        if not nums: return 0
        return max_consecutive
            