# Leetcode Link: https://leetcode.com/problems/spiral-matrix/

# **************** Python Solution ***********************

# ---------- Question ----------
# Given an m x n matrix, return all elements in spiral order.
#
# Example:
#   Input: [[1,2,3],[4,5,6],[7,8,9]]
#   Output: [1,2,3,6,9,8,7,4,5]

# ---------- Approach ----------
# Layer-by-layer — use four boundaries (top, bottom, left, right) and traverse:
#   1. Left → Right along top row
#   2. Top → Bottom along right column
#   3. Right → Left along bottom row (if rows remain)
#   4. Bottom → Top along left column (if columns remain)
# Shrink boundaries after each direction.
#
# Time Complexity : O(m * n) — visit each element once
# Space Complexity: O(1) — ignoring the output

class Solution:
    def spiralOrder(self, matrix):
        result = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # Traverse right
            for c in range(left, right + 1):
                result.append(matrix[top][c])
            top += 1

            # Traverse down
            for r in range(top, bottom + 1):
                result.append(matrix[r][right])
            right -= 1

            # Traverse left (only if rows remain)
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    result.append(matrix[bottom][c])
                bottom -= 1

            # Traverse up (only if columns remain)
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    result.append(matrix[r][left])
                left += 1

        return result
