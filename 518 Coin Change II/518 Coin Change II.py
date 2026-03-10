# Leetcode Link: https://leetcode.com/problems/coin-change-ii/
# **************** Python Solution ***********************
# ---------- Question ----------
# Given coins and amount, return number of COMBINATIONS that make up the amount.
# Example: amount=5, coins=[1,2,5] -> 4
# ---------- Approach ----------
# DP: iterate coins in outer loop (ensures combinations not permutations).
# dp[x] += dp[x - coin].
# Time: O(amount * |coins|) | Space: O(amount)
class Solution:
    def change(self, amount: int, coins) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1  # One way to make amount 0
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]
        return dp[amount]
