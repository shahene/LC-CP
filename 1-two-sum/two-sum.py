class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_target_map = {}
        for i in range(len(nums)):
            num_target_map[target - nums[i]] = i
        for i in range(len(nums)):
            if nums[i] in num_target_map and i != num_target_map[nums[i]]:
                return [i, num_target_map[nums[i]]]