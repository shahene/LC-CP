class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        given an array nums of size n, return the majority element
        majority element is the element that appears more than [n / 2] times
        '''
        current_el, count_el = nums[0], 1
        for i in range(1, len(nums)):
            if current_el != nums[i]:
                count_el -= 1
            else:
                count_el += 1
            if count_el == 0:
                current_el = nums[i]
                count_el += 1
        return current_el