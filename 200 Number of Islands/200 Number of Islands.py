# Leetcode Link: https://leetcode.com/problems/number-of-islands/
# **************** Python Solution ***********************
# ---------- Question ----------
# Given a 2D grid of '1's (land) and '0's (water), count the number of islands.
# An island is surrounded by water and formed by connecting adjacent lands.
# Example: grid=[["1","1","0"],["1","1","0"],["0","0","1"]] -> 2
# ---------- Approach ----------
# DFS flood fill: for each unvisited land cell, start DFS to mark the entire island.
# Time: O(m*n) | Space: O(m*n) recursion stack
class Solution:
    def numIslands(self, grid) -> int:
        if not grid: return 0
        rows, cols = len(grid), len(grid[0])
        islands = 0
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
                return
            grid[r][c] = '0'  # Mark as visited
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                dfs(r + dr, c + dc)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1
                    dfs(r, c)  # Sink the entire island
        return islands
