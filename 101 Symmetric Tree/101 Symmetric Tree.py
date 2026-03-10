# Most asked problems at FAANG companies: https://docs.google.com/spreadsheets/d/1hzP8j7matoUiJ15N-RhsL5Dmig8_E3aP/edit#gid=1377915986
# Leetcode Link: https://leetcode.com/problems/symmetric-tree/
# Video Solution: https://www.youtube.com/watch?v=NeSeH2ECZUw

# **************** Python Solution ***********************

# ---------- Question ----------
# Given the root of a binary tree, check whether it is a mirror of itself (symmetric).
#
# Example:
#   Input: root = [1,2,2,3,4,4,3]  ->  Output: True

# ---------- Approach ----------
# Recursive mirror check — two subtrees are mirrors if:
#   1. Both are None
#   2. Their root values are equal
#   3. Left-of-left mirrors right-of-right, and right-of-left mirrors left-of-right
#
# Time Complexity : O(n)
# Space Complexity: O(h) — recursion depth

class Solution:
    def isSymmetric(self, root) -> bool:
        if root is None:
            return True
        return self.isMirror(root.left, root.right)

    def isMirror(self, left, right) -> bool:
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        return (left.val == right.val and
                self.isMirror(left.left, right.right) and   # Outer pair
                self.isMirror(left.right, right.left))      # Inner pair
