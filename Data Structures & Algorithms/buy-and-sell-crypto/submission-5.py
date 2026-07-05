# Brute Force, nested for loops, exhaustive test of all solutions
# A non profitable situation is one where the values in the array are sorted in 
# descending order
# For an O(n) solution, iterate through the list updating the minimum value
# and then compute the profit with the subsequent value


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        lowest_price = 101

        for price in prices:
            lowest_price = min(lowest_price,price)
            max_profit = max(price - lowest_price, max_profit)
            

        return max_profit
        