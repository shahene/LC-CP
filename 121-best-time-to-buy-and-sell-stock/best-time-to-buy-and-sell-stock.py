class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        list of prices where prices[i] is the price of a stock on a given day i
        choose single i to buy stock and choose different i to sell stock
        return maximum profit

        [7, 1, 5, 3, 6, 4]
        choose i = 0, p = 7 to "buy"
        i = 1, p = 
        '''
        l = 0
        max_profit = -math.inf
        for r in range(len(prices)):
            if prices[r] - prices[l] < 0:
                l = r
            else:
                max_profit = max(max_profit, prices[r] - prices[l])
        return 0 if max_profit == -math.inf else max_profit
        
        
