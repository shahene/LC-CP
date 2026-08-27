class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        [10,1,10,10,10]
        '''
        l, r = 0, len(nums) - 1
        minimum = math.inf
        while l <= r:
            mid = (l + r) // 2
            if nums[l] < nums[mid]:
                minimum = min(minimum, nums[l])
                l = mid + 1
            elif nums[l] == nums[mid]:
                minimum = min(minimum, nums[l])
                l += 1
            else:
                minimum = min(minimum, nums[mid])
                r = mid - 1
        return minimum