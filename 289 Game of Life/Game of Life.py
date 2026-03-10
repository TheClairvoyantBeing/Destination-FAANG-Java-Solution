# Leetcode Link: https://leetcode.com/problems/game-of-life/
# **************** Python Solution ***********************
# ---------- Question ----------
# Implement Conway's Game of Life in-place:
# - Live cell with 2-3 live neighbors survives, otherwise dies
# - Dead cell with exactly 3 live neighbors becomes live
# ---------- Approach ----------
# Use intermediate states: -1 = was alive, now dead. 2 = was dead, now alive.
# This preserves original state for neighbor counting. Final pass normalizes values.
# Time: O(m*n) | Space: O(1)
class Solution:
    def gameOfLife(self, board) -> None:
        rows, cols = len(board), len(board[0])
        directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        for r in range(rows):
            for c in range(cols):
                live = sum(1 for dr, dc in directions
                           if 0 <= r+dr < rows and 0 <= c+dc < cols
                           and abs(board[r+dr][c+dc]) == 1)
                if board[r][c] == 1 and (live < 2 or live > 3):
                    board[r][c] = -1   # Was live, now dead
                if board[r][c] == 0 and live == 3:
                    board[r][c] = 2    # Was dead, now live
        for r in range(rows):
            for c in range(cols):
                board[r][c] = 1 if board[r][c] > 0 else 0  # Normalize
