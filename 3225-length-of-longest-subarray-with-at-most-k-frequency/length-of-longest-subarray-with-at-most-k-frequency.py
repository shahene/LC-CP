class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        length_longest, l = 0, 0
        num_counter = collections.defaultdict(int)
        for r in range(len(nums)):
            number = nums[r]
            num_counter[number] += 1
            while num_counter[number] > k:
                left_number = nums[l]
                num_counter[left_number] -= 1
                l += 1
            length_longest = max(length_longest, r - l + 1)
        return length_longest