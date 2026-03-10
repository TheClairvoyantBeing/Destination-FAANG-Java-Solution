# Leetcode Link: https://leetcode.com/problems/largest-rectangle-in-histogram/

# **************** Python Solution ***********************

# ---------- Question ----------
# Given an array of integers heights representing the histogram's bar heights,
# find the area of the largest rectangle in the histogram.
#
# Example:
#   Input: heights = [2,1,5,6,2,3]
#   Output: 10
#   Explanation: The largest rectangle has area 5 * 2 = 10 (bars at indices 2 and 3)

# ---------- Approach ----------
# Monotonic Stack — maintain a stack of (index, height) in increasing order.
# When a shorter bar is encountered, pop taller bars and calculate their max area
# extending left to the popped bar's start index.
#
# Time Complexity : O(n) — each bar is pushed and popped at most once
# Space Complexity: O(n) — stack

class Solution:
    def largestRectangleArea(self, heights) -> int:
        stack = []    # Stack of (start_index, height)
        max_area = 0

        for i, h in enumerate(heights):
            start = i
            # Pop bars taller than current — they can't extend further right
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                max_area = max(max_area, height * (i - idx))
                start = idx  # Current bar can extend left to popped bar's start
            stack.append((start, h))

        # Remaining bars in stack extend to the end of the histogram
        for idx, height in stack:
            max_area = max(max_area, height * (len(heights) - idx))

        return max_area
