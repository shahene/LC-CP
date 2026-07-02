class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        '''
        n minutes
        customers of length n
        customers[i] => number of customers that enter the store at the start of the ith minute
        and all of those customers leave the store at the end of that minute

        grumpy[i] => bookstore owner is grumpy at ith minute if 1 and 0 otherwise

        if grumpy[i] == 1: customers are not satisfied
        else: they are satisfied


        bookstore owners knows a secret technique to remain not grumpy for minutes consecutive minutes
        can only be used once

        return maximum number of customers that can be satisfied throughout the day 

        key question: which consecutive minutes should we use the technique on
        we can keep running sum of total
        if grumpy[i] == 1: add to total else
        keep separate variable for running sum max if grumpy[i] = 0 for each valid "window"
        that max is what we add to our total maximum number of customers

        Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3

        '''
        max_customers = 0
        running_sum, valid_window_sum = 0, 0
        l = 0
        for r in range(len(customers)):
            customer_num, grumpy_yn = customers[r], grumpy[r]
            if grumpy_yn == 0:
                max_customers += customer_num
            else:
                valid_window_sum += customer_num
            if r >= minutes - 1:
                running_sum = max(running_sum, valid_window_sum)
                left_customer = customers[l]
                grumpy_left = grumpy[l]
                if grumpy_left == 1:
                    valid_window_sum -= left_customer
                l += 1
        

        max_customers += running_sum
            
        return max_customers