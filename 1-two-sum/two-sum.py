class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_target_map = {}
        for i, n in enumerate(nums):
            num_target_map[target - n] = i
        for i, n in enumerate(nums):
            if n in num_target_map and num_target_map[n] != i:
                return [i, num_target_map[n]]