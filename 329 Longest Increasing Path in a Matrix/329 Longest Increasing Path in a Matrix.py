# Leetcode Link: https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
# **************** Python Solution ***********************
# ---------- Question ----------
# Given m x n integers matrix, return the length of the longest increasing path.
# Example: matrix=[[9,9,4],[6,6,8],[2,1,1]] -> 4 (path: 1->2->6->9)
# ---------- Approach ----------
# DFS with memoization: for each cell, explore all 4 directions where value increases.
# Cache results to avoid recomputation.
# Time: O(m*n) | Space: O(m*n)
class Solution:
    def longestIncreasingPath(self, matrix) -> int:
        if not matrix: return 0
        rows, cols = len(matrix), len(matrix[0])
        memo = {}
        def dfs(r, c):
            if (r, c) in memo: return memo[(r, c)]
            result = 1
            for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                    result = max(result, 1 + dfs(nr, nc))
            memo[(r, c)] = result
            return result
        return max(dfs(r, c) for r in range(rows) for c in range(cols))
