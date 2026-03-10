# Leetcode Link: https://leetcode.com/problems/detect-squares/
# **************** Python Solution ***********************
# ---------- Question ----------
# Design DetectSquares: add(point) adds a point, count(point) returns number of ways to
# form an axis-aligned square with the query point.
# ---------- Approach ----------
# Store point counts in a dict. For each query (px, py), iterate over all points with same x
# coordinate. The side length determines where the other two corners must be.
# Time: O(n) per count | Space: O(n)
from collections import defaultdict
class DetectSquares:
    def __init__(self):
        self.point_count = defaultdict(int)
        self.points = []
    def add(self, point) -> None:
        self.point_count[tuple(point)] += 1
        self.points.append(point)
    def count(self, point) -> int:
        px, py = point
        result = 0
        for x, y in self.points:
            if abs(px - x) != abs(py - y) or x == px or y == py:
                continue  # Must form a non-zero square
            # Check if the other two corners exist
            result += self.point_count[(x, py)] * self.point_count[(px, y)]
        return result
