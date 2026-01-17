class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix, output = [], [0] * len(nums), []
        total = 1
        for n in nums:
            total *= n
            prefix.append(total)
        total = 1
        for i in range(len(nums) - 1, -1, -1):
            total *= nums[i]
            postfix[i] = total
        for i in range(len(prefix)):
            if i == 0 and i < len(prefix) - 1:
                output.append(postfix[i+1])
            elif i == len(prefix) - 1:
                output.append(prefix[i - 1])
            else:
                output.append(prefix[i-1] * postfix[i+1])
        return output
            