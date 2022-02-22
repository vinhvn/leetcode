class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_price = -1
        max_profit = 0
        
        for p in prices:
            if p < min_price:
                min_price = p
                max_price = 0
            elif p > max_price:
                max_price = p
                max_profit = max(max_profit, max_price - min_price)
        
        return max_profit