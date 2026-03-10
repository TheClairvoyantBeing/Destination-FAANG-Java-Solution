# Leetcode Link: https://leetcode.com/problems/longest-common-subsequence/
# **************** Python Solution ***********************
# ---------- Question ----------
# Given two strings, return the length of their longest common subsequence. (Duplicate entry)
# ---------- Approach ----------
# Same as problem 1143. 2D DP approach.
# Time: O(m*n) | Space: O(m*n)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[m][n]
