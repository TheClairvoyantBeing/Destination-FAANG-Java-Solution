# Leetcode Link: https://leetcode.com/problems/invert-binary-tree/
# **************** Python Solution ***********************
# ---------- Question ----------
# Given the root of a binary tree, invert the tree (mirror it) and return the root.
# Example: [4,2,7,1,3,6,9] -> [4,7,2,9,6,3,1]
# ---------- Approach ----------
# Recursive: swap left and right children, then recursively invert each subtree.
# Time: O(n) | Space: O(h)
class Solution:
    def invertTree(self, root):
        if not root:
            return None
        root.left, root.right = root.right, root.left  # Swap children
        self.invertTree(root.left)    # Recurse on left
        self.invertTree(root.right)   # Recurse on right
        return root
