# Leetcode Link: https://leetcode.com/problems/valid-sudoku/

# **************** Python Solution ***********************

# ---------- Question ----------
# Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be
# validated according to: each row, each column, and each of the nine 3x3 sub-boxes
# must contain the digits 1-9 without repetition.
#
# Example:
#   Input: (valid board)  ->  Output: True

# ---------- Approach ----------
# Use sets to track seen digits for each row, column, and 3x3 box.
# Box index = (row // 3) * 3 + (col // 3)
#
# Time Complexity : O(1) — fixed 9x9 board (81 cells)
# Space Complexity: O(1) — fixed number of sets

class Solution:
    def isValidSudoku(self, board) -> bool:
        rows = [set() for _ in range(9)]   # Track digits in each row
        cols = [set() for _ in range(9)]   # Track digits in each column
        boxes = [set() for _ in range(9)]  # Track digits in each 3x3 box

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue
                box_idx = (r // 3) * 3 + c // 3
                if val in rows[r] or val in cols[c] or val in boxes[box_idx]:
                    return False  # Duplicate found
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_idx].add(val)

        return True
