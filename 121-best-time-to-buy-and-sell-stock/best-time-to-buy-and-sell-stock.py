class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        choose a single day to buy one stock
        choose a different day in the future to sell that stock
        return maximum profit you can achieve from this transaction.
        [7,1,5,3,6,4]

        '''
        if len(prices) == 1: return 0
        l, max_profit = 0, 0
        for r in range(1, len(prices)):
            if prices[r] < prices[l]:
                l = r
            else:
                max_profit = max(max_profit, prices[r] - prices[l])
        return max_profit
        