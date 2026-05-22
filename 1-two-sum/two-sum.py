class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        target = num1 + num2
        num2 = target - num1
        store target - current_num as keys in hashmap
        w index of (current_num) num1 as value
        '''
        complement_map = {}
        for i, n in enumerate(nums):
            complement_map[target - n] = i
        for i, n in enumerate(nums):
            if n in complement_map and i != complement_map[n]:
                return [i, complement_map[n]]
                
        