# Leetcode Link: https://leetcode.com/problems/combination-sum-ii/

# **************** Python Solution ***********************

# ---------- Question ----------
# Given a collection of candidate numbers and a target number, find all unique
# combinations where the candidate numbers sum to target. Each number may only
# be used once. The solution set must not contain duplicate combinations.
#
# Example:
#   Input: candidates = [10,1,2,7,6,1,5], target = 8
#   Output: [[1,1,6],[1,2,5],[1,7],[2,6]]

# ---------- Approach ----------
# Sort + Backtracking — sort the array, then backtrack. Skip duplicates at each
# level to avoid repeated combinations. Each element can only be used once (i+1).
#
# Time Complexity : O(2^n) — each element is either included or not
# Space Complexity: O(n) — recursion depth

class Solution:
    def combinationSum2(self, candidates, target: int):
        candidates.sort()  # Sort to handle duplicates easily
        result = []

        def backtrack(start, combo, total):
            if total == target:
                result.append(combo[:])
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                # Skip duplicates at the same decision level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                combo.append(candidates[i])
                backtrack(i + 1, combo, total + candidates[i])  # i+1 = no reuse
                combo.pop()

        backtrack(0, [], 0)
        return result
