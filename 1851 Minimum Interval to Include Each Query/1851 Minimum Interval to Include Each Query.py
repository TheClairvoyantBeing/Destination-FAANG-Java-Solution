# Leetcode Link: https://leetcode.com/problems/minimum-interval-to-include-each-query/
# **************** Python Solution ***********************
# ---------- Question ----------
# Given intervals and queries, for each query find the size of the smallest interval containing it.
# Return -1 if no interval contains the query.
# ---------- Approach ----------
# Sort intervals by start and queries by value. Use min-heap of (size, right_end).
# For each query, add all intervals with start <= query, remove expired ones, then peek.
# Time: O(n log n + q log q) | Space: O(n + q)
import heapq
class Solution:
    def minInterval(self, intervals, queries):
        intervals.sort()
        sorted_queries = sorted(enumerate(queries), key=lambda x: x[1])
        heap = []  # (interval_size, right_end)
        result = [-1] * len(queries)
        i = 0
        for qi, q in sorted_queries:
            # Add all intervals that start <= query
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(heap, (r - l + 1, r))
                i += 1
            # Remove intervals that end before query
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            if heap:
                result[qi] = heap[0][0]
        return result
