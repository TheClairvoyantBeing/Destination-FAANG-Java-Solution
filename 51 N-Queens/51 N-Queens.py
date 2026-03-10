# Leetcode Link: https://leetcode.com/problems/n-queens/

# **************** Python Solution ***********************

# ---------- Question ----------
# Place n queens on an n x n chessboard such that no two queens attack each other.
# Return all distinct solutions. Each solution is a board configuration.
#
# Example:
#   Input: n = 4
#   Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]

# ---------- Approach ----------
# Backtracking — place queens row by row. Track attacked columns, positive diagonals
# (row+col) and negative diagonals (row-col) using sets for O(1) lookup.
#
# Time Complexity : O(n!) — at most n choices for first row, n-1 for second, etc.
# Space Complexity: O(n^2) — for the board

class Solution:
    def solveNQueens(self, n: int):
        result = []
        cols = set()        # Columns under attack
        pos_diag = set()    # Positive diagonals (row + col)
        neg_diag = set()    # Negative diagonals (row - col)
        board = [['.' ] * n for _ in range(n)]

        def backtrack(row):
            if row == n:
                result.append([''.join(r) for r in board])
                return
            for col in range(n):
                if col in cols or (row + col) in pos_diag or (row - col) in neg_diag:
                    continue  # This position is under attack
                # Place queen
                cols.add(col)
                pos_diag.add(row + col)
                neg_diag.add(row - col)
                board[row][col] = 'Q'

                backtrack(row + 1)

                # Remove queen (backtrack)
                cols.remove(col)
                pos_diag.remove(row + col)
                neg_diag.remove(row - col)
                board[row][col] = '.'

        backtrack(0)
        return result
