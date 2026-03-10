# Leetcode Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# **************** Python Solution ***********************
# ---------- Question ----------
# Given array prices where prices[i] is the price on day i, find the maximum profit from
# one buy and one sell. You must buy before you sell. Return 0 if no profit possible.
# Example: prices=[7,1,5,3,6,4] -> 5 (buy at 1, sell at 6)
# ---------- Approach ----------
# Track the minimum price seen so far. At each price, check if selling gives a new max profit.
# Time: O(n) | Space: O(1)
class Solution:
    def maxProfit(self, prices) -> int:
        min_price = float('inf')   # Lowest price seen so far
        max_profit = 0             # Best profit found
        for price in prices:
            if price < min_price:
                min_price = price                     # New lowest buy price
            elif price - min_price > max_profit:
                max_profit = price - min_price        # New best profit
        return max_profit
