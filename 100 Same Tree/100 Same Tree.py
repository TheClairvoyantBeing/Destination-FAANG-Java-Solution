# Leetcode Link: https://leetcode.com/problems/same-tree/
# Youtube Link: https://www.youtube.com/watch?v=yi7ym5R5aYI

# **************** Python Solution ***********************

# ---------- Question ----------
# Given the roots of two binary trees p and q, check if they are the same.
# Two binary trees are the same if they are structurally identical and have the same values.
#
# Example:
#   Input: p = [1,2,3], q = [1,2,3]  ->  Output: True

# ---------- Approach ----------
# Recursive comparison — both trees are same if:
#   1. Both roots are None (base case)
#   2. Neither is None, values are equal, and left/right subtrees are the same
#
# Time Complexity : O(n) — visit each node once
# Space Complexity: O(h) — recursion depth

class Solution:
    def isSameTree(self, p, q) -> bool:
        if p is None and q is None:
            return True   # Both empty
        if p is None or q is None:
            return False  # One empty, one not
        if p.val != q.val:
            return False  # Values differ
        # Recursively check left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
