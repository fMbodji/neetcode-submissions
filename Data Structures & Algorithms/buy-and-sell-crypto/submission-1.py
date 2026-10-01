class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        buy, sell= 0,1
        while sell < n:
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                max_profit = max(max_profit, profit)
            else:
                buy = sell
            sell += 1
        return max_profit

        