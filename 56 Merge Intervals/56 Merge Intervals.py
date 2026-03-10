# Leetcode Link: https://leetcode.com/problems/merge-intervals/

# **************** Python Solution ***********************

# ---------- Question ----------
# Given an array of intervals, merge all overlapping intervals and return an
# array of the non-overlapping intervals.
#
# Example:
#   Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
#   Output: [[1,6],[8,10],[15,18]]

# ---------- Approach ----------
# Sort by start time, then iterate. If the current interval overlaps with the
# last merged interval, extend it; otherwise, add a new interval.
#
# Time Complexity : O(n log n) — dominated by sorting
# Space Complexity: O(n) — for the merged result

class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]

        for start, end in intervals[1:]:
            if start <= merged[-1][1]:  # Overlapping
                merged[-1][1] = max(merged[-1][1], end)  # Extend
            else:
                merged.append([start, end])  # Non-overlapping

        return merged
