class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current, maximum = 0, 0
        for i in range(1, len(prices)):
            delta = prices[i] - prices[i-1]
            current += delta
            if current < 0:
                current = 0;
            maximum = max(maximum, current)
        return maximum