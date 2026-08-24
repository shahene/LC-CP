class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        odd_i, even_i = 1, 0
        for n in nums:
            if n % 2 != 0:
                res[odd_i] = n
                odd_i += 2
            else:
                res[even_i] = n
                even_i += 2
        return res
        
