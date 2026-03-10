# Leetcode Link: https://leetcode.com/problems/combination-sum/

# **************** Python Solution ***********************

# ---------- Question ----------
# Given an array of distinct integers candidates and a target integer target,
# return all unique combinations of candidates where the chosen numbers sum to target.
# The same number may be chosen an unlimited number of times.
#
# Example:
#   Input: candidates = [2,3,6,7], target = 7
#   Output: [[2,2,3],[7]]

# ---------- Approach ----------
# Backtracking — at each step, either include the current candidate (can reuse it)
# or move to the next candidate. Prune when total exceeds target.
#
# Time Complexity : O(N^(T/M)) — N candidates, T target, M min candidate value
# Space Complexity: O(T/M) — recursion depth

class Solution:
    def combinationSum(self, candidates, target: int):
        result = []

        def backtrack(start, combo, total):
            if total == target:
                result.append(combo[:])  # Found a valid combination
                return
            if total > target:
                return  # Exceeded target — prune

            for i in range(start, len(candidates)):
                combo.append(candidates[i])
                # Pass i (not i+1) because we can reuse the same element
                backtrack(i, combo, total + candidates[i])
                combo.pop()  # Undo choice (backtrack)

        backtrack(0, [], 0)
        return result
