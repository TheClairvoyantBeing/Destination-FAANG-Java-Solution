# Leetcode Link: https://leetcode.com/problems/graph-valid-tree/
# **************** Python Solution ***********************
# ---------- Question ----------
# Given n nodes (0 to n-1) and edges, check if they form a valid tree.
# A valid tree: connected, no cycles, exactly n-1 edges.
# ---------- Approach ----------
# Union-Find: a graph is a tree if it has exactly n-1 edges and no cycle (all unions succeed).
# Time: O(E * α(n)) ≈ O(E) | Space: O(n)
class Solution:
    def validTree(self, n: int, edges) -> bool:
        if len(edges) != n - 1:
            return False  # Tree must have exactly n-1 edges
        parent = list(range(n))
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]  # Path compression
                x = parent[x]
            return x
        def union(x, y):
            px, py = find(x), find(y)
            if px == py: return False  # Cycle detected
            parent[px] = py
            return True
        return all(union(u, v) for u, v in edges)
