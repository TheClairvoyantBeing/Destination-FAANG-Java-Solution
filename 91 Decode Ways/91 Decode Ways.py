# Leetcode Link: https://leetcode.com/problems/decode-ways/

# **************** Python Solution ***********************

# ---------- Question ----------
# A message containing letters A-Z can be encoded: 'A' -> "1", 'B' -> "2", ..., 'Z' -> "26".
# Given a string s containing only digits, return the number of ways to decode it.
#
# Example:
#   Input: s = "226"  ->  Output: 3
#   Explanation: "226" can be decoded as "BZ"(2 26), "VF"(22 6), or "BBF"(2 2 6)

# ---------- Approach ----------
# Dynamic Programming — dp[i] = number of ways to decode s[0..i-1].
# At each position, check if the single digit (1-9) and two digits (10-26) are valid.
#
# Time Complexity : O(n)
# Space Complexity: O(n) — DP array

class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0  # Cannot start with '0'

        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1  # Base case: empty string has 1 decoding
        dp[1] = 1  # First character (we know it's not '0')

        for i in range(2, n + 1):
            # Single digit decoding (1-9)
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]
            # Two digit decoding (10-26)
            two_digit = int(s[i - 2:i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i - 2]

        return dp[n]
