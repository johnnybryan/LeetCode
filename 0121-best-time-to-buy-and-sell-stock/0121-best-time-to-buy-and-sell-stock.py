class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_profit, max_profit = 0, 0
        for i in range(1, len(prices)):
            delta = prices[i] - prices[i - 1]
            cur_profit += delta
            if cur_profit < 0:
                cur_profit = 0
            max_profit = max(cur_profit, max_profit)
        return max_profit
            