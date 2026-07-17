class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        given an array of integer nums
        input: nums array and target
        output: indices of two numbers such that they add up to target

        match => since we are returning indices, it would not be ideal to sort the array
              => can use a hash map
              => nums[i] + nums[j] = target
              => nums[j] = target - nums[i]
              => store key as (target - nums[i])
              => if we find match, make sure indices don't match in case of duplicates that add up to target
              => assume solution exists
              => can do it one pass 
        '''
        complement_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if num in complement_map and i != complement_map[num]:
                return [i, complement_map[num]]
            complement_map[complement] = i