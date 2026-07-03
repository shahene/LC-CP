class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        res = []
        num_counter = collections.Counter(nums)
        for n in nums:
            if num_counter[n] == 1 and n + 1 not in num_counter and n - 1 not in num_counter:
                res.append(n)
        return res