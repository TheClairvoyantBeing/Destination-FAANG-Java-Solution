# Leetcode Link: https://leetcode.com/problems/surrounded-regions/
# **************** Python Solution ***********************
# ---------- Question ----------
# Given an m x n board with 'X' and 'O', capture all regions surrounded by 'X'.
# A region is captured by flipping all 'O's into 'X's. 'O's on the border are not captured.
# ---------- Approach ----------
# Reverse thinking: mark border-connected 'O's as safe ('S'), then flip remaining 'O's to 'X',
# and restore 'S' back to 'O'.
# Time: O(m*n) | Space: O(m*n) recursion stack
class Solution:
    def solve(self, board) -> None:
        if not board or not board[0]:
            return
        rows, cols = len(board), len(board[0])
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
                return
            board[r][c] = 'S'  # Mark as safe (border-connected)
            dfs(r + 1, c); dfs(r - 1, c); dfs(r, c + 1); dfs(r, c - 1)
        # Mark border-connected O's
        for r in range(rows):
            for c in range(cols):
                if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1) and board[r][c] == 'O':
                    dfs(r, c)
        # Flip: O -> X (captured), S -> O (restored)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'S':
                    board[r][c] = 'O'
