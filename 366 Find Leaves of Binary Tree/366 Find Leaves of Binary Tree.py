# Leetcode Link: https://leetcode.com/problems/find-leaves-of-binary-tree/
# **************** Python Solution ***********************
# ---------- Question ----------
# Collect leaves level by level until the tree is empty.
# Example: [1,2,3,4,5] -> [[4,5,3],[2],[1]]
# ---------- Approach ----------
# DFS computing height from leaf (leaf=0). Group nodes by height.
# Time: O(n) | Space: O(n)
class Solution:
    def findLeaves(self, root):
        result = []
        def dfs(node):
            if not node: return -1
            level = max(dfs(node.left), dfs(node.right)) + 1
            if level == len(result):
                result.append([])
            result[level].append(node.val)
            return level
        dfs(root)
        return result
