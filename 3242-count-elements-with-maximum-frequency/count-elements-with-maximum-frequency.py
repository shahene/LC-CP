class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        
        num_counter = collections.Counter(nums)
        max_ = -math.inf
        total = 0
        for n in num_counter:
            if num_counter[n] > max_:
                max_ = num_counter[n]
                total = max_
            elif num_counter[n] == max_:
                total += max_
        
        return total