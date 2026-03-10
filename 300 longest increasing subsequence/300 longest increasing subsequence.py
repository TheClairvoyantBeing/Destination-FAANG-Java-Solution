# Leetcode Link: https://leetcode.com/problems/longest-increasing-subsequence/
# **************** Python Solution ***********************
# ---------- Question ----------
# Given an integer array, return the length of the longest strictly increasing subsequence.
# Example: nums=[10,9,2,5,3,7,101,18] -> 4 ([2,3,7,101])
# ---------- Approach ----------
# DP: dp[i] = length of LIS ending at index i. For each i, check all j < i.
# Time: O(n^2) | Space: O(n)
class Solution:
    def lengthOfLIS(self, nums) -> int:
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
