class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bs_recursive(arr, target, l, r):
            if l > r:
                return -1
            mid = l + (r - l) // 2
            if nums[mid] > target:
                return bs_recursive(arr, target, l, mid - 1)
            elif nums[mid] < target:
                return bs_recursive(arr, target, mid + 1, r)
            else:
                return mid
            
        l, r = 0, len(nums) - 1
        return bs_recursive(nums, target, l, r)