# Leetcode Link: https://leetcode.com/problems/jump-game/

# **************** Python Solution ***********************

# ---------- Question ----------
# You are given an integer array nums. You are initially at the first index.
# Each element represents your maximum jump length at that position.
# Return true if you can reach the last index.
#
# Example:
#   Input: nums = [2,3,1,1,4]  ->  Output: True
#   Input: nums = [3,2,1,0,4]  ->  Output: False

# ---------- Approach ----------
# Greedy (backwards) — start with the goal at the last index. Iterate backwards;
# if the current index can reach the goal, move the goal to the current index.
# If goal reaches index 0, we can make it.
#
# Time Complexity : O(n)
# Space Complexity: O(1)

class Solution:
    def canJump(self, nums) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i  # This position can reach the goal; make it the new goal

        return goal == 0
