class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = math.inf

        for price in prices:
            if price < minPrice:
                minPrice = price
            maxProfit = max(maxProfit, price - minPrice)
        return maxProfit
