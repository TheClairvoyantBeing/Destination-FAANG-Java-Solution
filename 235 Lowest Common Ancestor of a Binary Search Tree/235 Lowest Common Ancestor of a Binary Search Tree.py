# Leetcode Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# **************** Python Solution ***********************
# ---------- Question ----------
# Given a BST and two nodes p and q, find their lowest common ancestor.
# Example: root=[6,2,8,0,4,7,9], p=2, q=8 -> 6
# ---------- Approach ----------
# Exploit BST property: if both p, q < root, LCA is in left subtree.
# If both > root, LCA is in right subtree. Otherwise, root is the LCA.
# Time: O(h) | Space: O(1)
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left    # Both in left subtree
            elif p.val > root.val and q.val > root.val:
                root = root.right   # Both in right subtree
            else:
                return root         # Split point = LCA
