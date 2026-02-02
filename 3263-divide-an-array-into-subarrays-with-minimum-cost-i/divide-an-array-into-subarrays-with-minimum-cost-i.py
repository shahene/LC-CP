class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        '''
        given an array of integers nums of length n
        cost - value of first element
        [3,4,1] -> cost = 3

        need to divide nums into 3 disjoint contiguous subarrays.
        return minimum possible sum of cost of these subarrays

        Input: nums = [1,2,3,12]
        -> 1, 2, 3 => 6

        Input: nums = [10,3,1,1]

        first value of array needs to be part of the cost of a subarray
        so that is set in stone,
        then just find the next 2 smallest elements and sum them up
        so total = nums[0]
        iterate from 1 to end of nums:
            find first_smallest, second_smallest
        add first_smallest and second_smallest to total
        return total
        O(n) time, O(1) space
        '''
        total_cost = nums[0]
        first_smallest, second_smallest = math.inf, math.inf
        for i in range(1, len(nums)):
            val = nums[i]
            if val < first_smallest:
                second_smallest = first_smallest
                first_smallest = val
            elif val < second_smallest:
                second_smallest = val
        total_cost += (first_smallest + second_smallest)
        return total_cost