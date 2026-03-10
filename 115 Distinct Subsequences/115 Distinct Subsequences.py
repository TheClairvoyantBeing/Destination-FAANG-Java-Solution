# Leetcode Link: https://leetcode.com/problems/distinct-subsequences/
# **************** Python Solution ***********************
# ---------- Question ----------
# Given strings s and t, return the number of distinct subsequences of s that equal t.
# Example: s="rabbbit", t="rabbit" -> 3
# ---------- Approach ----------
# 2D DP: dp[i][j] = number of ways s[0..i-1] can form t[0..j-1].
# If s[i-1]==t[j-1]: dp[i][j] = dp[i-1][j-1] (use this char) + dp[i-1][j] (skip it)
# Otherwise: dp[i][j] = dp[i-1][j] (skip s[i-1])
# Time: O(m*n) | Space: O(m*n)
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = 1  # Empty t can be formed from any prefix of s
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i - 1][j]  # Skip s[i-1]
                if s[i - 1] == t[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]  # Use s[i-1] to match t[j-1]
        return dp[m][n]
