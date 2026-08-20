class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        max_profit = total = 0
        for r in range(len(prices)):
            cur_profit = prices[r] - prices[l]
            if cur_profit >= max_profit:
                max_profit = cur_profit
            else:
                total += max_profit
                max_profit = 0
                l = r

        return total if max_profit == 0 else total + max_profit