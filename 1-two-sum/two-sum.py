class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement_map = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            complement_map[complement] = i
        for i in range(len(nums)):
            if nums[i] in complement_map and i != complement_map[nums[i]]:
                return [i, complement_map[nums[i]]]