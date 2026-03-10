# Most asked problems at FAANG companies: https://docs.google.com/spreadsheets/d/1hzP8j7matoUiJ15N-RhsL5Dmig8_E3aP/edit#gid=1377915986
# Leetcode Link: https://leetcode.com/problems/min-cost-to-connect-all-points/
# Video Solution: https://www.youtube.com/watch?v=mvwrT2A4p60
# **************** Python Solution ***********************
# ---------- Question ----------
# Given points on 2D plane, return min cost to connect all points. Cost between two points
# is Manhattan distance |xi-xj| + |yi-yj|.
# ---------- Approach ----------
# Prim's MST algorithm with min-heap. Start from point 0, greedily add closest unvisited point.
# Time: O(n^2 log n) | Space: O(n^2)
import heapq
class Solution:
    def minCostConnectPoints(self, points) -> int:
        n = len(points)
        in_mst = [False] * n
        heap = [(0, 0)]  # (distance, point_index)
        min_cost = 0
        points_connected = 0
        while points_connected < n:
            dist, curr = heapq.heappop(heap)
            if in_mst[curr]:
                continue
            in_mst[curr] = True
            min_cost += dist
            points_connected += 1
            for i in range(n):
                if not in_mst[i]:
                    distance = abs(points[curr][0] - points[i][0]) + abs(points[curr][1] - points[i][1])
                    heapq.heappush(heap, (distance, i))
        return min_cost
