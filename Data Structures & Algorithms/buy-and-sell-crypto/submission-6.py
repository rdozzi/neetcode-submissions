# Brute Force, nested for loops, exhaustive test of all solutions
# A non profitable situation is one where the values in the array are sorted in 
# descending order


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        max_profit = 0

        for i in range(n):
            for j in range(i+1,n):
                profit = prices[j] - prices[i]
                max_profit = max(profit, max_profit)
        
        return max_profit

        
        