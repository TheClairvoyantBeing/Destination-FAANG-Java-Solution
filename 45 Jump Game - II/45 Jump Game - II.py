# Leetcode Link: https://leetcode.com/problems/jump-game-ii/

# **************** Python Solution ***********************

# ---------- Question ----------
# You are given a 0-indexed array of integers where nums[i] represents the max
# jump length from that position. Return the minimum number of jumps to reach
# the last index. Guaranteed that you can reach nums[n-1].
#
# Example:
#   Input: nums = [2,3,1,1,4]  ->  Output: 2
#   Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

# ---------- Approach ----------
# BFS / Greedy — treat it as a BFS where each "level" is the range of indices
# reachable with the current number of jumps. Track the farthest reachable index
# and increment jumps when we reach the boundary of the current level.
#
# Time Complexity : O(n) — single pass
# Space Complexity: O(1)

class Solution:
    def jump(self, nums) -> int:
        jumps = 0           # Number of jumps taken
        current_end = 0     # End of the current jump's reach
        farthest = 0        # Farthest index reachable from current level

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == current_end:  # Reached the end of current level
                jumps += 1
                current_end = farthest

        return jumps
