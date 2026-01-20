class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_arr, postfix_arr = [], [1] * len(nums)
        output = []
        prefix, postfix = 1, 1
        for i in range(len(nums)):
            prefix *=  nums[i]
            prefix_arr.append(prefix)
        for i in range(len(nums) - 1, -1, -1):
            postfix *= nums[i]
            postfix_arr[i] = postfix
        for i in range(len(nums)):

            pre = prefix_arr[i-1] if i > 0 else 1
            post = postfix_arr[i+1] if i != len(postfix_arr) - 1 else 1
            output.append(pre * post)
        return output