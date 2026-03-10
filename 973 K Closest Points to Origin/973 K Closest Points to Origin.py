# Leetcode Link: https://leetcode.com/problems/k-closest-points-to-origin/
# **************** Python Solution ***********************
# ---------- Question ----------
# Given array of points, return the k closest to the origin (0,0).
# Example: points=[[1,3],[-2,2]], k=1 -> [[-2,2]]
# ---------- Approach ----------
# Max-heap of size k: push negated distances. If heap exceeds k, pop the farthest.
# Time: O(n log k) | Space: O(k)
import heapq
class Solution:
    def kClosest(self, points, k: int):
        heap = []
        for x, y in points:
            dist = x*x + y*y
            heapq.heappush(heap, (-dist, [x, y]))
            if len(heap) > k:
                heapq.heappop(heap)  # Remove farthest
        return [p for _, p in heap]
