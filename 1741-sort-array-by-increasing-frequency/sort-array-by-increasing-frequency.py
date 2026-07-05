class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        num_counter = collections.Counter(nums)
        nums.sort(key=lambda x: (num_counter[x], -x))

        return nums