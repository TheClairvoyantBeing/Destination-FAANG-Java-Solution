# Leetcode Link: https://leetcode.com/problems/set-matrix-zeroes/

# **************** Python Solution ***********************

# ---------- Question ----------
# Given an m x n integer matrix, if an element is 0, set its entire row and column
# to 0's. Must do it in-place.
#
# Example:
#   Input: [[1,1,1],[1,0,1],[1,1,1]]
#   Output: [[1,0,1],[0,0,0],[1,0,1]]

# ---------- Approach ----------
# Use the first row and first column as markers. First, record whether the first
# row/column themselves need zeroing. Then use them to mark other rows/columns.
#
# Time Complexity : O(m * n)
# Space Complexity: O(1) — uses the matrix itself as storage

class Solution:
    def setZeroes(self, matrix) -> None:
        rows, cols = len(matrix), len(matrix[0])
        first_row = any(matrix[0][j] == 0 for j in range(cols))
        first_col = any(matrix[i][0] == 0 for i in range(rows))

        # Use first row/col as markers for other cells
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0  # Mark row
                    matrix[0][j] = 0  # Mark column

        # Zero out cells based on markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Handle first row and column separately
        if first_row:
            for j in range(cols):
                matrix[0][j] = 0
        if first_col:
            for i in range(rows):
                matrix[i][0] = 0
