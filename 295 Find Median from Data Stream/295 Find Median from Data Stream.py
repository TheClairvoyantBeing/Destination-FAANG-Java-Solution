# Leetcode Link: https://leetcode.com/problems/find-median-from-data-stream/
# **************** Python Solution ***********************
# ---------- Question ----------
# Design a data structure that supports addNum(num) and findMedian() efficiently.
# ---------- Approach ----------
# Two heaps: max-heap (small) for lower half, min-heap (large) for upper half.
# Balance sizes so they differ by at most 1. Median is from the larger heap (or average).
# Time: O(log n) for add, O(1) for median | Space: O(n)
import heapq
class MedianFinder:
    def __init__(self):
        self.small = []  # Max-heap (negate values)
        self.large = []  # Min-heap
    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        if self.small and self.large and (-self.small[0]) > self.large[0]:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.large) > len(self.small) + 1:
            heapq.heappush(self.small, -heapq.heappop(self.large))
    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        return (-self.small[0] + self.large[0]) / 2.0
