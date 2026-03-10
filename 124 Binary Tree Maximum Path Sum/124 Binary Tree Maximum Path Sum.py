# Leetcode Link: https://leetcode.com/problems/binary-tree-maximum-path-sum/
# **************** Python Solution ***********************
# ---------- Question ----------
# Given root of a binary tree, return the maximum path sum. A path is any sequence of
# nodes connected by edges (doesn't need to pass through root).
# Example: root=[-10,9,20,null,null,15,7] -> 42 (path: 15->20->7)
# ---------- Approach ----------
# Post-order DFS. For each node, compute: max gain extending to parent (single branch),
# and update global max considering the path through this node (both branches).
# Time: O(n) | Space: O(h)
class Solution:
    def maxPathSum(self, root) -> int:
        self.max_sum = float('-inf')
        def dfs(node):
            if node is None:
                return 0
            left = max(dfs(node.left), 0)    # Ignore negative paths
            right = max(dfs(node.right), 0)
            # Path through this node (left -> node -> right)
            self.max_sum = max(self.max_sum, node.val + left + right)
            # Return max single-branch gain to parent
            return node.val + max(left, right)
        dfs(root)
        return self.max_sum
