# Leetcode Link: https://leetcode.com/problems/container-with-most-water/

# **************** Python Solution ***********************

# ---------- Question ----------
# You are given an integer array height of length n. There are n vertical lines drawn
# such that the two endpoints of the i-th line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container that holds the most water.
#
# Example:
#   Input: height = [1,8,6,2,5,4,8,3,7]
#   Output: 49

# ---------- Approach ----------
# Two-pointer technique — start with the widest container (left=0, right=n-1).
# Move the pointer pointing to the shorter line inward, since moving the taller
# line can never increase the area.
#
# Time Complexity : O(n) — single pass with two pointers
# Space Complexity: O(1)

class Solution:
    def maxArea(self, height) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            # Area = width * min height of the two lines
            area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, area)

            # Move the shorter line inward to potentially find a taller one
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
