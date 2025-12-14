class Solution:
    def findMin(self, nums: List[int]) -> int:
        # go right if left side is unsorted
        # go left otherwise
        l, r = 0, len(nums) - 1
        minimum = nums[0]
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]
