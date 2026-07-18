class Solution:
    def findGCD(self, nums: List[int]) -> int:
        # implement euclid's algorithm
        minimum, maximum = min(nums), max(nums)
        while minimum != maximum:
            if maximum > minimum:
                maximum -= minimum
            else:
                minimum -= maximum
        return minimum