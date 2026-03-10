# Leetcode Link: https://leetcode.com/problems/subsets/

# **************** Python Solution ***********************

# ---------- Question ----------
# Given an integer array nums of unique elements, return all possible subsets (power set).
# The solution must not contain duplicate subsets.
#
# Example:
#   Input: nums = [1,2,3]
#   Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

# ---------- Approach ----------
# Backtracking — at each index, make two choices: include or exclude the element.
# Build subsets incrementally.
#
# Time Complexity : O(n * 2^n) — 2^n subsets, each up to n elements
# Space Complexity: O(n) — recursion depth

class Solution:
    def subsets(self, nums):
        result = []

        def backtrack(start, path):
            result.append(path[:])  # Add current subset (including empty)
            for i in range(start, len(nums)):
                path.append(nums[i])       # Include nums[i]
                backtrack(i + 1, path)     # Recurse with remaining elements
                path.pop()                 # Exclude nums[i] (backtrack)

        backtrack(0, [])
        return result
