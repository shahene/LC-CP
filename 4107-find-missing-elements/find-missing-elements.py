class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        '''
        optimal approach uses boolean array
        instead of allocating a size of res to be largest

        '''
        res = []
        smallest, largest = min(nums), max(nums)
        seen = [False] * (largest - smallest + 1)
        for i in range(len(nums)):
            seen[nums[i] - smallest] = True
        for i, n in enumerate(seen):
            if not n: res.append(i + smallest)
        return res