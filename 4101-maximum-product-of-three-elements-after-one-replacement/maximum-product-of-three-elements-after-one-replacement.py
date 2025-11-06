class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] *= -1

        first_largest, first_index = -math.inf, -1
        second_largest, second_index = -math.inf, -2
        print(nums)
        
        for i in range(len(nums)):
            if nums[i] > first_largest:
                first_largest = nums[i]
                first_index = i
        for i in range(len(nums)):
            if nums[i] > second_largest and i != first_index:
                second_largest = nums[i]
        print(first_largest, second_largest)
        return first_largest * second_largest * (10**5)
        