# Leetcode Link: https://leetcode.com/problems/rotting-oranges/
# **************** Python Solution ***********************
# ---------- Question ----------
# Grid with 0 (empty), 1 (fresh orange), 2 (rotten). Each minute, rotten oranges infect
# adjacent fresh ones. Return minutes until no fresh oranges remain, or -1 if impossible.
# Example: grid=[[2,1,1],[1,1,0],[0,1,1]] -> 4
# ---------- Approach ----------
# Multi-source BFS from all rotten oranges. Track fresh count; if any remain, return -1.
# Time: O(m*n) | Space: O(m*n)
from collections import deque
class Solution:
    def orangesRotting(self, grid) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2: queue.append((r, c))
                elif grid[r][c] == 1: fresh += 1
        if fresh == 0: return 0
        minutes = 0
        while queue:
            minutes += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))
        return minutes - 1 if fresh == 0 else -1
