# Leetcode Link: https://leetcode.com/problems/burst-balloons/
# **************** Python Solution ***********************
# ---------- Question ----------
# Given n balloons with values, burst them to maximize coins. Bursting balloon i gives
# nums[left] * nums[i] * nums[right] coins. Example: nums=[3,1,5,8] -> 167
# ---------- Approach ----------
# Interval DP: dp[left][right] = max coins from bursting all balloons between left and right
# (exclusive). Think of balloon i as the LAST one to burst in the interval.
# Time: O(n^3) | Space: O(n^2)
class Solution:
    def maxCoins(self, nums) -> int:
        nums = [1] + nums + [1]  # Add boundary balloons
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for length in range(2, n):
            for left in range(0, n - length):
                right = left + length
                for i in range(left + 1, right):  # i = last balloon to burst
                    dp[left][right] = max(
                        dp[left][right],
                        dp[left][i] + dp[i][right] + nums[left] * nums[i] * nums[right]
                    )
        return dp[0][n - 1]
