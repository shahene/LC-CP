class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        [0, n]
        input: list which has unique elements in range
        [0, n]
        output: the number that is missing from this range

        match
        ^, |, &, ~
        '''
        nums.sort()
        for i in range(len(nums) + 1):
            if i == len(nums) or i != nums[i]:
                return i
        #