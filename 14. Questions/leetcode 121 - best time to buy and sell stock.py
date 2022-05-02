"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Question: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1 
        maxP = 0
        
        while r<len(prices):
            #profit?
            if prices[l] < prices[r]:
                profit = prices[r]-prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r = r+1
            
        return maxP 