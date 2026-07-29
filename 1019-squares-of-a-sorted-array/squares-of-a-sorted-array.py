class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        index = len(res) - 1
        l, r = 0, len(nums) - 1
        while l <= r:
            if (nums[l] * nums[l]) >= (nums[r] * nums[r]):
                res[index] = (nums[l] * nums[l])
                l += 1
            else:
                res[index] = (nums[r] * nums[r])
                r -= 1
            index -= 1
        return res