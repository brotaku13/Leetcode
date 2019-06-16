"""
Idea: maintain a min price variable and a max profit variable 
make one pass through the array setting the values as necessary
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit =  prices[i] - min_price
                
        return max_profit