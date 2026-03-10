# Leetcode Link: https://leetcode.com/problems/maximum-subarray/

# **************** Python Solution ***********************

# ---------- Question ----------
# Given an integer array nums, find the subarray with the largest sum and return its sum.
#
# Example:
#   Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
#   Output: 6
#   Explanation: The subarray [4,-1,2,1] has the largest sum 6.

# ---------- Approach ----------
# Kadane's Algorithm — maintain a running sum. If the running sum becomes negative,
# reset it to the current element (start a new subarray).
#
# Time Complexity : O(n) — single pass
# Space Complexity: O(1)

class Solution:
    def maxSubArray(self, nums) -> int:
        max_sum = nums[0]       # Best sum found so far
        current_sum = nums[0]   # Current subarray sum

        for i in range(1, len(nums)):
            # Either extend existing subarray or start a new one
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)

        return max_sum
