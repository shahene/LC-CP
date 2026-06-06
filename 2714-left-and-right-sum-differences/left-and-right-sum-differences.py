class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left_sum, right_sum = [0], [0]
        total = 0
        output = []
        for i in range(1, len(nums)):
            total += nums[i - 1]
            left_sum.append(total)
        total = 0
        for i in range(len(nums) - 2, -1, -1):
            total += nums[i+1]
            right_sum.append(total)
        print(left_sum, right_sum)
        j = len(nums) - 1
        for i in range(len(nums)):
            output.append(abs(left_sum[i] - right_sum[j]))
            j -= 1
        return output
        