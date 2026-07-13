class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_map = collections.Counter(nums)
        return len(num_map) < len(nums)