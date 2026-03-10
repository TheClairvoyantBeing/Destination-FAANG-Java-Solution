# Most asked problems at FAANG companies: https://docs.google.com/spreadsheets/d/1hzP8j7matoUiJ15N-RhsL5Dmig8_E3aP/edit#gid=1377915986
# Leetcode Link: https://leetcode.com/problems/regular-expression-matching/
# Video Solution: https://www.youtube.com/watch?v=VFQddcCP46c

# **************** Python Solution ***********************

# ---------- Question ----------
# Given an input string s and a pattern p, implement regular expression matching
# with support for '.' (matches any single character) and '*' (matches zero or more
# of the preceding element).
#
# Example:
#   Input: s = "aa", p = "a*"  ->  Output: True
#   Input: s = "ab", p = ".*"  ->  Output: True

# ---------- Approach ----------
# Dynamic Programming — dp[i][j] = True if s[0..i-1] matches p[0..j-1].
# Handle three cases for each pattern character:
#   1) '.' — matches any character
#   2) Exact match — s[i] == p[j]
#   3) '*' — either skip the pattern pair (zero occurrences) or consume one char
#
# Time Complexity : O(m * n) — where m = len(s), n = len(p)
# Space Complexity: O(m * n) — for the DP table

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if s is None or p is None:
            return False

        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True  # Empty string matches empty pattern

        # Handle patterns like a*, a*b*, a*b*c* that can match empty string
        for i in range(len(p)):
            if p[i] == '*' and dp[0][i - 1]:
                dp[0][i + 1] = True

        for i in range(len(s)):
            for j in range(len(p)):
                if p[j] == '.':                    # '.' matches any single char
                    dp[i + 1][j + 1] = dp[i][j]
                if p[j] == s[i]:                   # Exact character match
                    dp[i + 1][j + 1] = dp[i][j]
                if p[j] == '*':                    # '*' — zero or more of preceding
                    if p[j - 1] != s[i] and p[j - 1] != '.':
                        dp[i + 1][j + 1] = dp[i + 1][j - 1]  # Zero occurrences
                    else:
                        # dp[i+1][j]   — single occurrence
                        # dp[i][j+1]   — multiple occurrences
                        # dp[i+1][j-1] — zero occurrences
                        dp[i + 1][j + 1] = dp[i + 1][j] or dp[i][j + 1] or dp[i + 1][j - 1]

        return dp[len(s)][len(p)]
