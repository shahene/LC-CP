class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicateCatcher = set()
        for n in nums:
            if n in duplicateCatcher:
                return True
            duplicateCatcher.add(n)
        return False