class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        '''
        since constraints are small, you can check every single subarray
        '''
        num_distinct = len(set(nums))
        total = 0
        for i in range(len(nums)):
            subarr = set()
            subarr.add(nums[i])
            if len(subarr) == num_distinct:
                total += 1
            for j in range(i + 1, len(nums)):
                subarr.add(nums[j])
                if len(subarr) == num_distinct:
                    total += 1
        return total