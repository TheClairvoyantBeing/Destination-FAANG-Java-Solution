# Leetcode Link: https://leetcode.com/problems/pacific-atlantic-water-flow/
# **************** Python Solution ***********************
# ---------- Question ----------
# Given m x n heights, return cells from which water can flow to both Pacific and Atlantic oceans.
# Pacific touches top/left edges, Atlantic touches bottom/right edges.
# ---------- Approach ----------
# Reverse DFS from ocean borders: find cells reachable from Pacific, cells reachable from Atlantic.
# Answer = intersection.
# Time: O(m*n) | Space: O(m*n)
class Solution:
    def pacificAtlantic(self, heights):
        if not heights: return []
        rows, cols = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        def dfs(r, c, visit, prev):
            if (r,c) in visit or r<0 or r>=rows or c<0 or c>=cols or heights[r][c]<prev:
                return
            visit.add((r, c))
            for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
                dfs(r+dr, c+dc, visit, heights[r][c])
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])
            dfs(rows-1, c, atlantic, heights[rows-1][c])
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols-1, atlantic, heights[r][cols-1])
        return list(pacific & atlantic)
