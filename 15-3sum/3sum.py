class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        '''
        returning triplets [nums[i], nums[j], nums[k]]
        where nums[i] + nums[j] + nums[k] == 0.
        [1, 1, 1]
        => no solution so return empty array

        must not contain duplicate triplets
        so need to acount for duplicate elements somehow

        plan:
        sort nums
        fix nums[i]
        use 2 pointer to find -nums[i] as sum of two numbers
        because -nums[i] + nums[i] = 0
        after solution found, skip duplicate elements

        O(n^2) time complexity, O(n) space for sorting
        '''

        nums.sort()
        output = []
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            l, r = i + 1, len(nums) - 1 
            while l < r:
                current_sum = nums[i] + nums[l] + nums[r]
                if current_sum < 0:
                    l += 1
                elif current_sum > 0:
                    r -= 1
                else:
                    output.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < len(nums) and nums[l] == nums[l-1]:
                        l += 1
        return output
