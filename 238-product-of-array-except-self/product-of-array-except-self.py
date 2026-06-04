class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        get every value before nums[i] in the input array
        and every value after nums[i] in the input array
        multiply together

        O(n) time and space

        prefix and postfix arrays
        prefix = [1, 1, 2, 6]
        postfix = [24 12, 4, 1]
        '''
        prefix = [1]
        postfix = [0] * len(nums)
        output = []
        running_mult = 1
        for i in range(len(nums)):
            running_mult *= nums[i]
            prefix.append(running_mult)
        running_mult = 1
        index = len(postfix) - 1
        postfix[index] = 1
        index -= 1
        i = len(nums) - 1
        while i > 0:
            running_mult *= nums[i]
            postfix[index] = running_mult
            index -= 1
            i -= 1
        print(postfix)
        for a, b in zip(prefix, postfix):
            output.append(a * b)

        return output
