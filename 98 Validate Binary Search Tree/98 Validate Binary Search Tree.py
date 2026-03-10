# Leetcode Link: https://leetcode.com/problems/validate-binary-search-tree/

# **************** Python Solution ***********************

# ---------- Question ----------
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
# A valid BST is defined as:
#   - Left subtree contains only nodes with values < node's value
#   - Right subtree contains only nodes with values > node's value
#   - Both subtrees must also be valid BSTs
#
# Example:
#   Input: root = [2,1,3]  ->  Output: True
#   Input: root = [5,1,4,null,null,3,6]  ->  Output: False

# ---------- Approach ----------
# Recursive validation with bounds — each node must be within a valid range (low, high).
# For left children, update the upper bound. For right children, update the lower bound.
#
# Time Complexity : O(n) — visit each node once
# Space Complexity: O(h) — recursion depth (h = height of tree)

class Solution:
    def isValidBST(self, root) -> bool:
        def validate(node, low, high):
            if not node:
                return True  # Empty tree is valid
            if node.val <= low or node.val >= high:
                return False  # Node violates the range constraint
            # Left child must be < node.val, right child must be > node.val
            return (validate(node.left, low, node.val) and
                    validate(node.right, node.val, high))

        return validate(root, float('-inf'), float('inf'))
