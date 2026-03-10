# Leetcode Link: https://leetcode.com/problems/permutations/

# **************** Python Solution ***********************

# ---------- Question ----------
# Given an array nums of distinct integers, return all the possible permutations.
#
# Example:
#   Input: nums = [1,2,3]
#   Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# ---------- Approach ----------
# Backtracking — at each position, choose one of the remaining elements,
# add it to the current path, recurse, then undo the choice.
#
# Time Complexity : O(n * n!) — n! permutations, each takes O(n) to build
# Space Complexity: O(n) — recursion depth

class Solution:
    def permute(self, nums):
        result = []

        def backtrack(path, remaining):
            if not remaining:
                result.append(path[:])  # Found a complete permutation
                return
            for i in range(len(remaining)):
                path.append(remaining[i])
                # Exclude current element from remaining choices
                backtrack(path, remaining[:i] + remaining[i + 1:])
                path.pop()  # Backtrack

        backtrack([], nums)
        return result
