class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_profit, max_profit = 0, 0
        for i in range(1, len(prices)):
            difference = prices[i] - prices[i-1]
            cur_profit += difference
            if cur_profit < 0:
                cur_profit = 0
            max_profit = max(cur_profit, max_profit)
        return max_profit
            