# Leetcode Link: https://leetcode.com/problems/meeting-rooms/
# **************** Python Solution ***********************
# ---------- Question ----------
# Given array of meeting time intervals, determine if a person can attend all meetings.
# Example: intervals=[[0,30],[5,10],[15,20]] -> False (overlap)
# ---------- Approach ----------
# Sort by start time. If any meeting starts before the previous one ends, return False.
# Time: O(n log n) | Space: O(1)
class Solution:
    def canAttendMeetings(self, intervals) -> bool:
        intervals.sort(key=lambda x: x[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                return False  # Overlap detected
        return True
