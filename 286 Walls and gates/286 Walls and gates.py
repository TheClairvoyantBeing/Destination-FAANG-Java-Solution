# Leetcode Link: https://leetcode.com/problems/walls-and-gates/
# **************** Python Solution ***********************
# ---------- Question ----------
# Given a grid with 0 (gate), -1 (wall), INF (empty room), fill each empty room with distance
# to its nearest gate. Example: INF next to gate -> 1
# ---------- Approach ----------
# Multi-source BFS from all gates simultaneously. Each gate starts at distance 0.
# Time: O(m*n) | Space: O(m*n)
from collections import deque
class Solution:
    def wallsAndGates(self, rooms) -> None:
        if not rooms: return
        rows, cols = len(rooms), len(rooms[0])
        INF = 2147483647
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    queue.append((r, c))  # Add all gates as sources
        while queue:
            r, c = queue.popleft()
            for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and rooms[nr][nc] == INF:
                    rooms[nr][nc] = rooms[r][c] + 1
                    queue.append((nr, nc))
