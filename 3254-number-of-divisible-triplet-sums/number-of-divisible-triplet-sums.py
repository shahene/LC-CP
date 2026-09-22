class Solution:
    def divisibleTripletCount(self, nums: List[int], d: int) -> int:
        count = 0
        for i in range(len(nums) - 2):
            right = collections.Counter(ith_val % d for ith_val in nums[i+2:])
            for j in range(i + 1, len(nums) - 1):
                needed_remainder = -(nums[i] + nums[j]) % d
                count += right[needed_remainder]
                right[nums[j+1] % d] -= 1
        return count
