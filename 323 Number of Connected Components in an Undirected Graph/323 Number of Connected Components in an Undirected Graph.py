# Leetcode Link: https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
# **************** Python Solution ***********************
# ---------- Question ----------
# Given n nodes and edges, return the number of connected components.
# ---------- Approach ----------
# Union-Find: start with n components. Each successful union reduces count by 1.
# Time: O(E * alpha(n)) ~ O(E) | Space: O(n)
class Solution:
    def countComponents(self, n: int, edges) -> int:
        parent = list(range(n))
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]  # Path compression
                x = parent[x]
            return x
        components = n
        for u, v in edges:
            pu, pv = find(u), find(v)
            if pu != pv:
                parent[pu] = pv
                components -= 1
        return components
