class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        smallest, largest = min(nums), max(nums)
        res = [0] * largest
        for i in range(len(nums)):
            res[nums[i] - 1] = nums[i]
        missing_numbers = []
        for i in range(len(res)):
            if res[i] == 0 and i >= smallest - 1 and i <= largest - 1: 
                missing_numbers.append(i + 1)
        return missing_numbers