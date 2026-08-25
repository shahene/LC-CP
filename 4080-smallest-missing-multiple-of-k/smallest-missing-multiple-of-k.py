class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        num_map = collections.Counter(nums)
        for i in range(1, 101):
            if i % k == 0 and i not in num_map:
                return i
        return ((100 // k) + 1) * k

