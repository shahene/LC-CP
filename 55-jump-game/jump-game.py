class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        initially positioned at array's first inde
        and each element represent max jump length at that position
        return true if u ca reach the last index or false otherwise

        '''
        max_index, last_index = 0, len(nums) - 1
        
        for i, n in enumerate(nums):
            if i > max_index: return False
            current_max_index = i + n
            max_index = max(max_index, current_max_index)
        return max_index >= last_index