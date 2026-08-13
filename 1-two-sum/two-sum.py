import collections
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = collections.defaultdict(int)
        for i, n in enumerate(nums):
            num_map[nums[i]] = i
        for i, n in enumerate(nums):
            if (target - nums[i]) in num_map and i != num_map[target - nums[i]]:
                return [num_map[target - nums[i]], i]