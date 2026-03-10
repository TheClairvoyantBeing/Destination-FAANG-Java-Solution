# Leetcode Link: https://leetcode.com/problems/gas-station/
# **************** Python Solution ***********************
# ---------- Question ----------
# N gas stations in a circle. gas[i] is gas available, cost[i] is cost to travel to next.
# Find the starting station index for a complete circuit, or -1 if impossible.
# Example: gas=[1,2,3,4,5], cost=[3,4,5,1,2] -> 3
# ---------- Approach ----------
# Greedy: if total gas >= total cost, a solution exists. Track running total; if it goes
# negative, the answer must be AFTER this station.
# Time: O(n) | Space: O(1)
class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:
        if sum(gas) < sum(cost):
            return -1  # Not enough total gas
        total = 0
        start = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:       # Can't reach next station from current start
                total = 0
                start = i + 1   # Try starting from next station
        return start
