class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        given an integery arary nums, return all triplets 
        solution should not contain duplicate triplets
        nums[i] + nums[j] + nums[k] == 0
        sort nums
        use two pointers to find other two numbers
        skip duplicates (which would be same number at same position)
        '''
        nums.sort()
        solution_set = []
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i-1]: continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = nums[l] + nums[r] + nums[i]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    solution_set.append([nums[l], nums[r], nums[i]])
                    l += 1
                    r -= 1
                    while l < len(nums) and nums[l] == nums[l-1]:
                        l += 1
            

        return solution_set