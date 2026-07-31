class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        given an array prices where prices[i] is the price of given stock on ith day
        maximize profit by choosing 1 day to buy and different day to sell

        return max profit

        input: array of prices
        output: max profit after "buying" one day and "selling" afterwards

        can't sort because we rely on indices which govern the day that we are currently on
        condition for profit:
        
        buying day must be greater than selling day

        [7, 3, 2, 1, 6, 4]
        possible_buying_price = 7
        possible_selling_price = 1
        7 < 1: so move possible buying price to 3

        possible_buying_price = 3
        selling = 5, profit = 2
        selling = 1, possible_buying_price < selling:
        move possible_buying_price to selling price (1) 

        O(n) time + O(1)
        one pointer for buying price, one pointer for selling price
        
        edge cases: []
        '''
        l = max_profit = 0
        for r in range(1, len(prices)):
            if prices[r] < prices[l]:
                l = r
            else:
                max_profit = max(prices[r] - prices[l], max_profit)

        return max_profit