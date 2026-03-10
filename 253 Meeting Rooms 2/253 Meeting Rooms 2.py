# Leetcode Link: https://leetcode.com/problems/meeting-rooms-ii/
# **************** Python Solution ***********************
# ---------- Question ----------
# Given array of meeting intervals, find the minimum number of conference rooms required.
# Example: intervals=[[0,30],[5,10],[15,20]] -> 2
# ---------- Approach ----------
# Sort by start time, use min-heap of end times. If earliest ending room is free (end <= start),
# reuse it (pop). Otherwise, add a new room. Heap size = rooms needed.
# Time: O(n log n) | Space: O(n)
import heapq
class Solution:
    def minMeetingRooms(self, intervals) -> int:
        if not intervals: return 0
        intervals.sort(key=lambda x: x[0])
        heap = []  # Min-heap of room end times
        for interval in intervals:
            if heap and heap[0] <= interval[0]:
                heapq.heappop(heap)  # Reuse the room that ends earliest
            heapq.heappush(heap, interval[1])
        return len(heap)
