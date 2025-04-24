# Problem: Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        buy = math.inf

        for i in range(len(prices)):

            buy = min(buy,prices[i])
            temp = prices[i] - buy

            profit = max(profit,temp)
    
        return profit