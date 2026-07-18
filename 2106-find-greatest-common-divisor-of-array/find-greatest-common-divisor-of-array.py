class Solution:
    def findGCD(self, nums: List[int]) -> int:
        smallest, largest = min(nums), max(nums)
        gcd = 1
        for i in range(1, largest + 1):
            if smallest % i == 0 and largest % i == 0:
                gcd = i
        return gcd