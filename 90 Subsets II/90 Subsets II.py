# Leetcode Link: https://leetcode.com/problems/subsets-ii/

# **************** Python Solution ***********************

# ---------- Question ----------
# Given an integer array nums that may contain duplicates, return all possible
# subsets (the power set). The solution set must not contain duplicate subsets.
#
# Example:
#   Input: nums = [1,2,2]
#   Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

# ---------- Approach ----------
# Sort + Backtracking — sort the array to bring duplicates together. At each level,
# skip elements that are the same as the previous one to avoid duplicate subsets.
#
# Time Complexity : O(n * 2^n)
# Space Complexity: O(n) — recursion depth

class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()  # Sort to group duplicates
        result = []

        def backtrack(start, path):
            result.append(path[:])
            for i in range(start, len(nums)):
                # Skip duplicates at the same decision level
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return result
