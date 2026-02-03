class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        have hashmap that we go through at same time as we iterate
        through list:
        start with 0: 1 as base case
        if sum - k in map:
            add to res the number of times sum - k shows up
        add to its frequency in prefix sum
        prefix_sum  count
        return res
        '''
        res = 0
        prefix_map = {0: 1}
        current_sum = 0
        for n in nums:
            current_sum += n
            if current_sum - k in prefix_map:
                res += prefix_map[current_sum - k]
            if current_sum not in prefix_map:
                prefix_map[current_sum] = 0
            prefix_map[current_sum] += 1
            
        return res