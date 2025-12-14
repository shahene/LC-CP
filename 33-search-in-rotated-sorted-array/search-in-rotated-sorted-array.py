class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        at any one point: either left of mid or right of mid is sorted
        deduce which half target is in and move accordingly
        '''
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[l] <= nums[mid]:
                if target == nums[mid]:
                    return mid
                elif target <= nums[mid] and target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if target == nums[mid]:
                    return mid
                elif target <= nums[r] and target >= nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
        
                

