class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        
        '''
        res = nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
                res = min(nums[mid], res)
            else:
                r = mid - 1
                res = min(nums[mid], res)
                
        return min(nums[l], res)