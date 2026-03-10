# Leetcode Link: https://leetcode.com/problems/pascals-triangle/
# **************** Python Solution ***********************
# ---------- Question ----------
# Given numRows, generate the first numRows of Pascal's triangle.
# Example: numRows=5 -> [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# ---------- Approach ----------
# Build row by row. Each element = sum of two elements from the previous row.
# Time: O(numRows^2) | Space: O(numRows^2)
class Solution:
    def generate(self, numRows: int):
        triangle = []
        for i in range(numRows):
            row = [1] * (i + 1)         # Initialize row with 1s
            for j in range(1, i):       # Fill inner elements
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            triangle.append(row)
        return triangle
