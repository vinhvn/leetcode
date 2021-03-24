class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        min = prices[0]
        max = prices[1]
        profit = 0
        
        for i in range(1, len(prices)):
            price = prices[i]
            
            if price < min:
                min = price
                max = price
            
            if price >= max:
                max = price
                if max - min > profit:
                    profit = max - min
        
        return profit
