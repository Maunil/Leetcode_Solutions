class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_profit = 0 
        length = len(prices)
        
        for i in range(length):
            if min_price > prices[i]:
                min_price = prices[i]
            
            if prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
            
        return max_profit
            