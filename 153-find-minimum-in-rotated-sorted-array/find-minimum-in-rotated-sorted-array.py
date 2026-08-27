class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        [0, 1, 2, 4, 5, 6, 7]
        rotated 4 times
        [4, 5, 6, 7, 0, 1, 2]
        return miimum element in O(log n) time

        so binary search
        
        [nums[n-4], nums[n-3], nums[n-2], nums[n-1], nums[n-6], nums[n-5], nums[n-4]]
        '''
        minimum_val = math.inf
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[l] <= nums[mid]:
                minimum_val = min(minimum_val, nums[l])
                l = mid + 1
            else:
                minimum_val = min(minimum_val, nums[mid])
                r = mid - 1
        return minimum_val