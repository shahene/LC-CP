class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
        input: integer array, return true if any value appears at least twice in the array
        output: boolean (true for duplicate, false for non duplicate)

        
        '''
        return len(collections.Counter(nums)) < len(nums)