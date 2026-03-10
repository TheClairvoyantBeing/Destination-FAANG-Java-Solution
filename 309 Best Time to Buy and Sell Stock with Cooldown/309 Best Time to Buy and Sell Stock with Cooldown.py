# Leetcode Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
# **************** Python Solution ***********************
# ---------- Question ----------
# Buy and sell stocks with a 1-day cooldown after selling. Maximize profit.
# Example: prices=[1,2,3,0,2] -> 3 (buy 1, sell 2, cooldown, buy 0, sell 2)
# ---------- Approach ----------
# State machine with 3 states: sold (just sold), held (holding stock), rest (cooldown/idle).
# sold = held + price, held = max(held, rest - price), rest = max(rest, prev_sold)
# Time: O(n) | Space: O(1)
class Solution:
    def maxProfit(self, prices) -> int:
        if len(prices) <= 1: return 0
        sold, held, rest = 0, float('-inf'), 0
        for price in prices:
            prev_sold = sold
            sold = held + price             # Sell today
            held = max(held, rest - price)  # Buy today or keep holding
            rest = max(rest, prev_sold)     # Rest or come off cooldown
        return max(sold, rest)
