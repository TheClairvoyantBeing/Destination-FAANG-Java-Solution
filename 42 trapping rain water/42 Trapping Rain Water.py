# Leetcode Link: https://leetcode.com/problems/trapping-rain-water/

# **************** Python Solution ***********************

# ---------- Question ----------
# Given n non-negative integers representing an elevation map where the width of
# each bar is 1, compute how much water it can trap after raining.
#
# Example:
#   Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
#   Output: 6

# ---------- Approach ----------
# Two-pointer technique — maintain left_max and right_max while moving the pointers
# inward. Water at any position = min(left_max, right_max) - height[i].
#
# Time Complexity : O(n) — single pass
# Space Complexity: O(1)

class Solution:
    def trap(self, height) -> int:
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        total = 0

        while left < right:
            if height[left] < height[right]:
                left_max = max(left_max, height[left])
                total += left_max - height[left]  # Water trapped at this position
                left += 1
            else:
                right_max = max(right_max, height[right])
                total += right_max - height[right]
                right -= 1

        return total
