# Leetcode Link: https://leetcode.com/problems/insert-interval/

# **************** Python Solution ***********************

# ---------- Question ----------
# You are given an array of non-overlapping intervals sorted by start time.
# Insert a new interval into the intervals and merge if necessary.
#
# Example:
#   Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
#   Output: [[1,5],[6,9]]

# ---------- Approach ----------
# Three phases:
#   1. Add all intervals that end before newInterval starts
#   2. Merge all overlapping intervals with newInterval
#   3. Add all remaining intervals
#
# Time Complexity : O(n) — single pass
# Space Complexity: O(n) — for the result

class Solution:
    def insert(self, intervals, newInterval):
        result = []
        i = 0

        # Phase 1: Add intervals that come entirely before newInterval
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # Phase 2: Merge overlapping intervals with newInterval
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval = [min(newInterval[0], intervals[i][0]),
                           max(newInterval[1], intervals[i][1])]
            i += 1
        result.append(newInterval)  # Add the merged interval

        # Phase 3: Add remaining intervals
        while i < len(intervals):
            result.append(intervals[i])
            i += 1

        return result
