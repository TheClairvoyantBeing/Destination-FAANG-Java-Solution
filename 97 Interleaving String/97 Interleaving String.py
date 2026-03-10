# Leetcode Link: https://leetcode.com/problems/interleaving-string/

# **************** Python Solution ***********************

# ---------- Question ----------
# Given strings s1, s2, and s3, determine whether s3 is formed by an interleaving of s1 and s2.
# An interleaving preserves the left-to-right order within each string.
#
# Example:
#   Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
#   Output: True

# ---------- Approach ----------
# 2D Dynamic Programming — dp[i][j] = True if s3[0..i+j-1] can be formed by
# interleaving s1[0..i-1] and s2[0..j-1].
#
# Time Complexity : O(m * n) — where m = len(s1), n = len(s2)
# Space Complexity: O(m * n) — DP table

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False  # Lengths must match

        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[0][0] = True  # Empty strings interleave to form empty string

        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                # Take character from s1
                if i > 0 and s1[i - 1] == s3[i + j - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j]
                # Take character from s2
                if j > 0 and s2[j - 1] == s3[i + j - 1]:
                    dp[i][j] = dp[i][j] or dp[i][j - 1]

        return dp[len(s1)][len(s2)]
