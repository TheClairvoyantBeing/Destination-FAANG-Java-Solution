# Leetcode Link: https://leetcode.com/problems/swim-in-rising-water/
# **************** Python Solution ***********************
# ---------- Question ----------
# n x n grid where grid[i][j] = elevation. Swim from (0,0) to (n-1,n-1).
# At time t, you can visit cells with elevation <= t. Find minimum time.
# ---------- Approach ----------
# Modified Dijkstra: use min-heap. The "cost" of a path = max elevation encountered.
# Time: O(n^2 log n) | Space: O(n^2)
import heapq
class Solution:
    def swimInWater(self, grid) -> int:
        n = len(grid)
        visited = {(0, 0)}
        heap = [(grid[0][0], 0, 0)]
        result = 0
        while heap:
            t, r, c = heapq.heappop(heap)
            result = max(result, t)
            if r == n-1 and c == n-1: return result
            for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < n and 0 <= nc < n and (nr,nc) not in visited:
                    visited.add((nr, nc))
                    heapq.heappush(heap, (grid[nr][nc], nr, nc))
        return result
