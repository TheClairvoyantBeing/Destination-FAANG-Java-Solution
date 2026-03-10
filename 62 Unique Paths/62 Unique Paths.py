# Leetcode Link: https://leetcode.com/problems/unique-paths/

# **************** Python Solution ***********************

# ---------- Question ----------
# A robot is located at the top-left corner of an m x n grid.
# It can only move right or down. How many unique paths exist to the bottom-right?
#
# Example:
#   Input: m = 3, n = 7  ->  Output: 28

# ---------- Approach ----------
# Dynamic Programming (space-optimized) — use a 1D array representing the current row.
# Each cell = paths from above + paths from the left.
#
# Time Complexity : O(m * n)
# Space Complexity: O(n) — single row

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n  # First row: all cells have 1 path

        for i in range(1, m):        # For each subsequent row
            for j in range(1, n):    # For each cell (skip first column, always 1)
                dp[j] += dp[j - 1]   # Paths = from above (dp[j]) + from left (dp[j-1])

        return dp[n - 1]
