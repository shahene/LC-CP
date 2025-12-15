class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix & suffix arrays
        prefix, suffix = [1], [0] * len(nums)
        suffix[-1] = 1
        suffix_tot = 1
        for i in range(len(nums) - 1):
            prefix.append(nums[i] * prefix[i])
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = (suffix_tot * nums[i + 1])
            suffix_tot = suffix[i]
        output = []
        for p, s in zip(prefix, suffix):
            output.append(p * s)
        return output