import math
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        '''
        3sum but keep track of min abs value (tot - target)
        '''
        nums.sort()
        possible_closest = min_val = math.inf

        for i in range(len(nums) - 1):
            l, r = i + 1, len(nums) - 1
            while l < r:
                tot = nums[l] + nums[r] + nums[i]

                if tot == target: return target
                
                if abs(tot - target) < min_val:
                    min_val = abs(tot - target)
                    possible_closest = tot

                if tot < target:
                    l += 1
                else:
                    r -= 1
        return possible_closest