class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = 10001
        ans = 0
        maxProfit = 0
        for price in prices:
            if price < minPrice:
                minPrice = price
                
            elif price - minPrice > maxProfit:
                ans += (price - minPrice)
                maxProfit = 0
                minPrice = price 
            
        return ans