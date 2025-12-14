class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        '''
        use binary search to find target
        then expand left pointers and right pointers until nums[i] != target
        '''
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                l_index, r_index = mid, mid
                while l_index >= 0 and nums[l_index] == target:
                    l_index -= 1
                while r_index < len(nums) and nums[r_index] == target:
                    r_index += 1
                left_starting, right_starting = mid, mid
                if nums[l_index + 1] == target:
                    left_starting = l_index + 1
                right_starting = mid
                if nums[r_index - 1] == target:
                    right_starting = r_index - 1
                return [left_starting, right_starting]
        return [-1, -1]