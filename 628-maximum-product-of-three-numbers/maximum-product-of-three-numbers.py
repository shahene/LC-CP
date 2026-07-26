import math
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # get three biggest numbers
        # take their product
        '''
        can sort then take first three numbers and multiply product => O(n) time + O(n) space
        or 3 passes => O(3n) + O(1) space
        1 pass => O(n) + O(1)

        1 pass:
        keep track of three elements

        first_biggest = nums[0]
        second_biggest = -math.inf
        third_biggest = -math.inf

        if current_element > first_biggest:
            tmp = first_biggest
            first_biggest = current_element
            tmp_1 = second_biggest
            second_biggest = first_biggest
            third_biggest = tmp_1
        elif current_element > second_biggest:
            tmp = second_biggest 
            second_biggest = current_element
            third_biggest = tmp
        elif current_element > third_biggest:
            third_biggest = current_element
        
        return first_biggest * second_biggest * third_biggest
        '''
        first_biggest = -math.inf
        second_biggest, third_biggest = -math.inf, -math.inf
        first_neg, second_neg = math.inf, math.inf
        for i in range(len(nums)):

            current_element = nums[i]

            if current_element < 0 and current_element < first_neg:
                first_neg, second_neg = current_element, first_neg
                print(first_neg)
            elif current_element < 0 and current_element < second_neg:
                print(second_neg)
                second_neg = current_element

            if current_element > first_biggest:
                first_biggest, second_biggest, third_biggest = current_element, first_biggest, second_biggest
            elif current_element > second_biggest:
                second_biggest, third_biggest = current_element, second_biggest
            elif current_element > third_biggest:
                third_biggest = current_element
        
        product_res = first_biggest * second_biggest * third_biggest

        if first_neg != math.inf and second_neg != math.inf:
            product_res = max(product_res, first_neg * second_neg * first_biggest)
        print(f"first_neg: {first_neg} second_neg: {second_neg} first_biggest = {first_biggest}")
        return product_res
