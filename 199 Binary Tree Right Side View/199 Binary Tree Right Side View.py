# Leetcode Link: https://leetcode.com/problems/binary-tree-right-side-view/
# **************** Python Solution ***********************
# ---------- Question ----------
# Given root, return the values of nodes visible from the right side (last node at each level).
# Example: root=[1,2,3,null,5,null,4] -> [1,3,4]
# ---------- Approach ----------
# BFS level-by-level, add the last node of each level to the result.
# Time: O(n) | Space: O(n)
from collections import deque
class Solution:
    def rightSideView(self, root):
        if not root: return []
        result = []
        queue = deque([root])
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                if i == level_size - 1:    # Last node in this level
                    result.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        return result
