# Leetcode Link: https://leetcode.com/problems/rotate-image/

# **************** Python Solution ***********************

# ---------- Question ----------
# Rotate an n x n 2D matrix by 90 degrees clockwise. Do it in-place.
#
# Example:
#   Input:  [[1,2,3],[4,5,6],[7,8,9]]
#   Output: [[7,4,1],[8,5,2],[9,6,3]]

# ---------- Approach ----------
# Two-step approach:
#   1. Transpose the matrix (swap rows and columns)
#   2. Reverse each row
# transpose + reverse row = 90° clockwise rotation
#
# Time Complexity : O(n^2)
# Space Complexity: O(1) — in-place

class Solution:
    def rotate(self, matrix) -> None:
        n = len(matrix)

        # Step 1: Transpose — swap matrix[i][j] with matrix[j][i]
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row
        for i in range(n):
            matrix[i].reverse()
