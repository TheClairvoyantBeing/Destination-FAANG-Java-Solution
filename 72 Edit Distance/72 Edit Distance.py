# Leetcode Link: https://leetcode.com/problems/edit-distance/

# **************** Python Solution ***********************

# ---------- Question ----------
# Given two strings word1 and word2, return the minimum number of operations
# (insert, delete, replace) to convert word1 to word2.
#
# Example:
#   Input: word1 = "horse", word2 = "ros"  ->  Output: 3
#   Explanation: horse -> rorse (replace h with r) -> rose (remove r) -> ros (remove e)

# ---------- Approach ----------
# Dynamic Programming — dp[i][j] = min operations to convert word1[0..i-1] to word2[0..j-1].
# If characters match: dp[i][j] = dp[i-1][j-1] (no operation needed).
# Otherwise: 1 + min(insert, delete, replace).
#
# Time Complexity : O(m * n)
# Space Complexity: O(m * n) — DP table

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Base cases: converting empty string to/from another
        for i in range(m + 1):
            dp[i][0] = i  # Delete all characters from word1
        for j in range(n + 1):
            dp[0][j] = j  # Insert all characters into word1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]  # Characters match — no cost
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],      # Delete from word1
                        dp[i][j - 1],      # Insert into word1
                        dp[i - 1][j - 1]   # Replace
                    )

        return dp[m][n]
