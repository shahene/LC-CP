class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        num_counter = collections.Counter(nums)
        while original in num_counter:
            num_counter[original] -= 1
            original *= 2
        return original