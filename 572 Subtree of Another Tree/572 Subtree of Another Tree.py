# Leetcode Link: https://leetcode.com/problems/subtree-of-another-tree/
# **************** Python Solution ***********************
# ---------- Question ----------
# Given roots of two binary trees, check if subRoot is a subtree of root.
# ---------- Approach ----------
# For each node in root, check if the subtree rooted there is identical to subRoot.
# Time: O(m * n) | Space: O(h)
class Solution:
    def isSubtree(self, root, subRoot) -> bool:
        if not subRoot: return True
        if not root: return False
        if self.isSameTree(root, subRoot): return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    def isSameTree(self, p, q) -> bool:
        if not p and not q: return True
        if not p or not q or p.val != q.val: return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
