class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        '''
        given two integers n and t
        return smallest number greater than or equal to n such that the product of its digits
        is divisble by t

        n and t can be from a relatively small range, so a brute force solution should be acceptable
        just efficiently extract digits
        O(1) time and O(1) space
        we can start at for (n, 101):
            first number where product of digits is divisible by t
            return that number

        digit extraction:
        let's say i = 15
        to get 5, we can do 15 % 10
        and then 15 // 10 for remaining digit
        '''
        for i in range(n, 101):
            possible_number, digit_product = i, 1

            while possible_number:
                digit_product *= (possible_number % 10)
                possible_number = possible_number // 10
            if digit_product % t == 0: return i
            
