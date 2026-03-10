# Leetcode Link: https://leetcode.com/problems/counting-bits/
# **************** Python Solution ***********************
# ---------- Question ----------
# For every number i in [0, n], count the number of 1s in its binary representation.
# Example: n=5 -> [0,1,1,2,1,2]
# ---------- Approach ----------
# DP with offset: dp[i] = 1 + dp[i - offset], where offset is the largest power of 2 <= i.
# Time: O(n) | Space: O(n)
class Solution:
    def countBits(self, n: int):
        dp = [0] * (n + 1)
        offset = 1
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp
