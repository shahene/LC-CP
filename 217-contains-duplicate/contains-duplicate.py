class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_counter = collections.Counter(nums)
        if len(num_counter) < len(nums): return True
        return False