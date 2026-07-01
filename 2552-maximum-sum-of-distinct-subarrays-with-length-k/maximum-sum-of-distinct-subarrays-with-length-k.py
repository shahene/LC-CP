class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        maximum_sum, running_sum = 0, 0
        nums_map = collections.defaultdict(int)
        l = 0

        for r in range(len(nums)):
            number = nums[r]
            nums_map[number] += 1
            running_sum += number
            if r - l + 1 > k - 1:
                if len(nums_map) == k:
                    maximum_sum = max(maximum_sum, running_sum)
                left_number = nums[l]
                nums_map[left_number] -= 1
                if nums_map[left_number] == 0:
                    del nums_map[left_number]
                running_sum -= left_number
                l += 1
                

        return maximum_sum