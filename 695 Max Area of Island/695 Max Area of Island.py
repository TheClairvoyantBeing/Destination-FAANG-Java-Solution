# Leetcode Link: https://leetcode.com/problems/max-area-of-island/
# **************** Python Solution ***********************
# ---------- Question ----------
# Given a binary grid, return the area of the largest island (connected 1s).
# Example: grid with island of 4 connected 1s -> 4
# ---------- Approach ----------
# DFS flood fill: for each land cell, DFS counting area while marking visited.
# Time: O(m*n) | Space: O(m*n) recursion
class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        rows, cols = len(grid), len(grid[0])
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0
            grid[r][c] = 0  # Mark visited
            return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)
        return max((dfs(r,c) for r in range(rows) for c in range(cols)), default=0)
