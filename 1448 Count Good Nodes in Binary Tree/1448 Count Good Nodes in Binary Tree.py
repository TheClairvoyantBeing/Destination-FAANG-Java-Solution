# Most asked problems at FAANG companies: https://docs.google.com/spreadsheets/d/1hzP8j7matoUiJ15N-RhsL5Dmig8_E3aP/edit#gid=1377915986
# Leetcode Link: https://leetcode.com/problems/count-good-nodes-in-binary-tree/
# Video Solution: https://www.youtube.com/watch?v=AiCPoU8q2sU
# **************** Python Solution ***********************
# ---------- Question ----------
# A node is "good" if the path from root to it has no node with value greater than it.
# Count all good nodes. Example: root=[3,1,4,3,null,1,5] -> 4
# ---------- Approach ----------
# DFS tracking the maximum value seen along the path from root. If current >= max, it's good.
# Time: O(n) | Space: O(h)
class Solution:
    def goodNodes(self, root) -> int:
        def countGoodNodes(node, max_so_far):
            if not node:
                return 0
            count = 0
            if node.val >= max_so_far:
                count = 1
                max_so_far = node.val
            count += countGoodNodes(node.left, max_so_far)
            count += countGoodNodes(node.right, max_so_far)
            return count
        return countGoodNodes(root, float('-inf'))
