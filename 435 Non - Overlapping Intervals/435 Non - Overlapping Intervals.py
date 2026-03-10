# Leetcode Link: https://leetcode.com/problems/non-overlapping-intervals/
# **************** Python Solution ***********************
# ---------- Question ----------
# Given intervals, return minimum number of intervals to remove to make rest non-overlapping.
# Example: intervals=[[1,2],[2,3],[3,4],[1,3]] -> 1 (remove [1,3])
# ---------- Approach ----------
# Greedy: sort by end time. Keep intervals that end earliest (maximizes room for future ones).
# Count intervals whose start < previous end (must be removed).
# Time: O(n log n) | Space: O(1)
class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:
        intervals.sort(key=lambda x: x[1])
        count = 0
        prev_end = float('-inf')
        for start, end in intervals:
            if start >= prev_end:
                prev_end = end  # Keep this interval
            else:
                count += 1      # Remove this interval (overlaps)
        return count
