# Leetcode Link: https://leetcode.com/problems/clone-graph/
# **************** Python Solution ***********************
# ---------- Question ----------
# Given a reference to a node in a connected undirected graph, return a deep copy.
# ---------- Approach ----------
# DFS with hash map — map each original node to its clone. When visiting a node,
# clone it and recursively clone all its neighbors.
# Time: O(V + E) | Space: O(V)
class Solution:
    def cloneGraph(self, node):
        if not node:
            return None
        visited = {}  # Map: original node -> cloned node
        def dfs(n):
            if n in visited:
                return visited[n]
            clone = Node(n.val, [])
            visited[n] = clone
            for neighbor in n.neighbors:
                clone.neighbors.append(dfs(neighbor))
            return clone
        return dfs(node)
