import collections
class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        counter = collections.Counter(nums)
        if k == 1:
            max_sol = max((x for x, freq in counter.items() if freq == 1), default=-1)
            return max_sol
        if k == len(nums):
            max_sol = max(nums)
            return max_sol
        max_sol = -1
        if counter[nums[0]] == 1:
            max_sol = max(max_sol, nums[0])
        if counter[nums[-1]] == 1:
            max_sol = max(max_sol, nums[-1])
        return max_sol



    '''
    [3, 9, 2, 1, 7]
    {
        3: 1, 9: 2, 2: 3, 1: 1
        l = 1
        for i in range(2, 3):

    }
    '''
