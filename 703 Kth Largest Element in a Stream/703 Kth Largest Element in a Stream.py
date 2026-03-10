# Leetcode Link: https://leetcode.com/problems/kth-largest-element-in-a-stream/
# **************** Python Solution ***********************
# ---------- Question ----------
# Design a class that finds the k-th largest element in a stream.
# ---------- Approach ----------
# Min-heap of size k: top element is always the k-th largest.
# Time: O(log k) per add | Space: O(k)
import heapq
class KthLargest:
    def __init__(self, k: int, nums):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)
    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
