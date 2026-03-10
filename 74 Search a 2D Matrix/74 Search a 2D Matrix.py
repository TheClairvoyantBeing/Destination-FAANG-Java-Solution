# Leetcode Link: https://leetcode.com/problems/search-a-2d-matrix/

# **************** Python Solution ***********************

# ---------- Question ----------
# Given an m x n matrix where each row is sorted and the first element of each row
# is greater than the last element of the previous row, determine if a target exists.
#
# Example:
#   Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
#   Output: True

# ---------- Approach ----------
# Treat the matrix as a flattened sorted array and apply binary search.
# Convert 1D index to 2D: row = mid // cols, col = mid % cols.
#
# Time Complexity : O(log(m * n))
# Space Complexity: O(1)

class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1

        while left <= right:
            mid = (left + right) // 2
            val = matrix[mid // cols][mid % cols]  # Convert 1D index to 2D
            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
