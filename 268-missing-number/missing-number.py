class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        [0, n]
        input: list which has unique elements in range
        [0, n]
        output: the number that is missing from this range

        one approach besides sorting or hashmap
        is to compare sums ?


        
        #
        
        '''
        n = len(nums)
        return sum(range(n + 1)) - sum(nums)