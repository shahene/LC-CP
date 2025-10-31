class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        output = []
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j - 1 != i and nums[j] == nums[j-1]:
                    continue
                l, r = j + 1, len(nums) - 1
                while l < r:
                    total_sum = nums[l] + nums[r] + nums[j] + nums[i]
                    if total_sum < target:
                        l += 1
                    elif total_sum > target:
                        r -= 1
                    else:
                        output.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < len(nums) and nums[l] == nums[l-1]:
                            l += 1
        return output