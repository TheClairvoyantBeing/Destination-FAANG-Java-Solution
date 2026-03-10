# Leetcode Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/

# **************** Python Solution ***********************

# ---------- Question ----------
# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path
# from the root node down to the farthest leaf node.
#
# Example:
#   Input: root = [3,9,20,null,null,15,7]  ->  Output: 3

# ---------- Approach ----------
# Recursive DFS — the depth of a tree = 1 + max(depth of left subtree, depth of right subtree).
# Base case: empty tree has depth 0.
#
# Time Complexity : O(n) — visit each node once
# Space Complexity: O(h) — recursion depth (h = height)

class Solution:
    def maxDepth(self, root) -> int:
        if root is None:
            return 0
        # 1 (current node) + max depth of the deeper subtree
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
