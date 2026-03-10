# Leetcode Link: https://leetcode.com/problems/employee-free-time/
# **************** Python Solution ***********************
# ---------- Question ----------
# Given schedules of employees (list of intervals), find common free time intervals.
# ---------- Approach ----------
# Flatten and sort all intervals by start time. Find gaps between merged intervals.
# Time: O(n log n) | Space: O(n)
class Solution:
    def employeeFreeTime(self, schedule):
        intervals = sorted([iv for emp in schedule for iv in emp], key=lambda x: x.start)
        result = []
        prev_end = intervals[0].end
        for iv in intervals[1:]:
            if iv.start > prev_end:
                result.append(Interval(prev_end, iv.start))  # Gap = free time
            prev_end = max(prev_end, iv.end)
        return result
