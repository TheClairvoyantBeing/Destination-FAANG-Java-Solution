# Leetcode Link: https://leetcode.com/problems/target-sum/
# **************** Python Solution ***********************
# ---------- Question ----------
# Assign + or - to each number to make them sum to target. Count the number of ways.
# Example: nums=[1,1,1,1,1], target=3 -> 5
# ---------- Approach ----------
# DFS with memoization: at each index, branch into +nums[i] and -nums[i].
# Time: O(n * sum) | Space: O(n * sum)
class Solution:
    def findTargetSumWays(self, nums, target: int) -> int:
        memo = {}
        def dp(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in memo: return memo[(i, total)]
            memo[(i, total)] = dp(i+1, total+nums[i]) + dp(i+1, total-nums[i])
            return memo[(i, total)]
        return dp(0, 0)
