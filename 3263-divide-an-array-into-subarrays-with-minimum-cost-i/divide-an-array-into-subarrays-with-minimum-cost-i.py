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
        total = nums[0]
        first_smallest, second_smallest = math.inf, math.inf
        for i in range(1, len(nums)):
            current_number = nums[i]
            if current_number <= first_smallest:
                second_smallest = first_smallest
                first_smallest = current_number
            elif current_number > first_smallest and current_number <= second_smallest:
                second_smallest = current_number
        return total + first_smallest + second_smallest