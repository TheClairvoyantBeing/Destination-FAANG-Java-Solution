# Leetcode Link: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
# **************** Python Solution ***********************
# ---------- Question ----------
# Design an algorithm to serialize and deserialize a binary tree to/from a string.
# ---------- Approach ----------
# Pre-order DFS. Serialize: write node value or "N" for null. Deserialize: reconstruct
# using an index pointer advancing through the serialized values.
# Time: O(n) | Space: O(n)
class Codec:
    def serialize(self, root) -> str:
        result = []
        def dfs(node):
            if not node:
                result.append("N"); return
            result.append(str(node.val))
            dfs(node.left); dfs(node.right)
        dfs(root)
        return ",".join(result)
    def deserialize(self, data: str):
        vals = data.split(",")
        self.i = 0
        def dfs():
            if vals[self.i] == "N":
                self.i += 1; return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs(); node.right = dfs()
            return node
        return dfs()
