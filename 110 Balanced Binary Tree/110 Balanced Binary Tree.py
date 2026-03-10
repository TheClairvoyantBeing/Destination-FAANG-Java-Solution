# Leetcode Link: https://leetcode.com/problems/balanced-binary-tree/

# **************** Python Solution ***********************

# ---------- Question ----------
# Given a binary tree, determine if it is height-balanced.
# A height-balanced tree is one where the subtrees of every node differ in height by at most 1.
#
# Example:
#   Input: root = [3,9,20,null,null,15,7]  ->  Output: True
#   Input: root = [1,2,2,3,3,null,null,4,4]  ->  Output: False

# ---------- Approach ----------
# Bottom-up recursion — compute height of each subtree. If any subtree is unbalanced
# (height difference > 1), propagate -1 upward to indicate failure.
#
# Time Complexity : O(n) — each node visited once
# Space Complexity: O(h) — recursion depth

class Solution:
    def isBalanced(self, root) -> bool:
        def height(node):
            if node is None:
                return 0
            left_h = height(node.left)
            right_h = height(node.right)
            # If either subtree is unbalanced or current node is unbalanced
            if left_h == -1 or right_h == -1 or abs(left_h - right_h) > 1:
                return -1  # Signal that tree is unbalanced
            return 1 + max(left_h, right_h)

        return height(root) != -1
