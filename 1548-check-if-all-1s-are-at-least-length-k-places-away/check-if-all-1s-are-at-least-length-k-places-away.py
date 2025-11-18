class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev = math.inf
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                if prev != math.inf and count < k: return False
                prev = 0
                count = 0
            else:
                count += 1

        return True