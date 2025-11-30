class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        minimum = math.inf
        total = 0
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                minimum = min(r - l + 1, minimum)
                total -= nums[l]
                l += 1
        
        return minimum if minimum != math.inf else 0