# Leetcode Link: https://leetcode.com/problems/diameter-of-binary-tree/
# **************** Python Solution ***********************
# ---------- Question ----------
# Find the length of the diameter of a binary tree (longest path between any two nodes).
# Example: root=[1,2,3,4,5] -> 3 (path: 4->2->1->3 or 4->2->5)
# ---------- Approach ----------
# DFS: at each node, diameter through it = left_depth + right_depth.
# Track global maximum. Return depth (not diameter) to parent.
# Time: O(n) | Space: O(h)
class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        self.diameter = 0
        def depth(node):
            if not node: return 0
            left = depth(node.left)
            right = depth(node.right)
            self.diameter = max(self.diameter, left + right)
            return 1 + max(left, right)
        depth(root)
        return self.diameter
