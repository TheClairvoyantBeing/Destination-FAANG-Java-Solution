# Leetcode Link: https://leetcode.com/problems/climbing-stairs/

# **************** Python Solution ***********************

# ---------- Question ----------
# You are climbing a staircase with n steps. Each time you can climb 1 or 2 steps.
# In how many distinct ways can you climb to the top?
#
# Example:
#   Input: n = 3  ->  Output: 3
#   Explanation: Three ways — (1+1+1), (1+2), (2+1)

# ---------- Approach ----------
# Dynamic Programming (Fibonacci pattern) — ways(n) = ways(n-1) + ways(n-2).
# Space-optimized to O(1) by only keeping the last two values.
#
# Time Complexity : O(n)
# Space Complexity: O(1)

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        prev2, prev1 = 1, 2  # Base cases: 1 step = 1 way, 2 steps = 2 ways
        for _ in range(3, n + 1):
            curr = prev1 + prev2  # Current step = sum of previous two
            prev2 = prev1
            prev1 = curr

        return prev1
