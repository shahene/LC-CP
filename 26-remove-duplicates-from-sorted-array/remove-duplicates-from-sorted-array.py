class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index, next_num_index = 1, 1
        prev = nums[0]
        k = 1
        while index < len(nums):
            if nums[index] != prev:
                nums[next_num_index] = nums[index]
                next_num_index += 1
                prev = nums[index]
                k += 1
            index += 1
        return k
        
        