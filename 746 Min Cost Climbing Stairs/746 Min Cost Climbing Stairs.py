# Leetcode Link: https://leetcode.com/problems/min-cost-climbing-stairs/
# **************** Python Solution ***********************
# ---------- Question ----------
# Array where cost[i] is the cost to step on stair i. Start from step 0 or 1.
# Pay the cost to move 1 or 2 steps. Find minimum cost to reach the top.
# Example: cost=[10,15,20] -> 15 (start at step 1, pay 15, jump 2 steps)
# ---------- Approach ----------
# DP: cost[i] += min(cost[i-1], cost[i-2]). Answer = min(cost[-1], cost[-2]).
# Time: O(n) | Space: O(1) — modifies input
class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        for i in range(2, len(cost)):
            cost[i] += min(cost[i - 1], cost[i - 2])
        return min(cost[-1], cost[-2])
