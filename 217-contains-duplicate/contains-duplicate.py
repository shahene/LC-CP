class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicate_checker = collections.Counter(nums)
        for n in duplicate_checker.values():
            if n >= 2: return True
        return False