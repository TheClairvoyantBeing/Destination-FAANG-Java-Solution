# LeetCode link: https://leetcode.com/problems/binary-tree-level-order-traversal/

# **************** Python Solution ***********************

# ---------- Question ----------
# Given the root of a binary tree, return the level order traversal of its nodes' values
# (i.e., from left to right, level by level).
#
# Example:
#   Input: root = [3,9,20,null,null,15,7]
#   Output: [[3],[9,20],[15,7]]

# ---------- Approach ----------
# DFS with level tracking — pass the current level as a parameter. When visiting a node,
# add its value to the list at the corresponding level index.
#
# Time Complexity : O(n) — visit each node once
# Space Complexity: O(n) — for the result list

class Solution:
    def levelOrder(self, root):
        ans = []
        if root is None:
            return ans

        def order(node, level):
            if len(ans) == level:
                ans.append([])       # Start a new level
            ans[level].append(node.val)
            if node.left:
                order(node.left, level + 1)
            if node.right:
                order(node.right, level + 1)

        order(root, 0)
        return ans
