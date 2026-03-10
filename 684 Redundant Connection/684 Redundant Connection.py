# Leetcode Link: https://leetcode.com/problems/redundant-connection/
# **************** Python Solution ***********************
# ---------- Question ----------
# Given a graph that is a tree plus one extra edge, find and return the redundant edge.
# ---------- Approach ----------
# Union-Find: process edges in order. The first edge that connects two already-connected
# nodes is the redundant one.
# Time: O(n * alpha(n)) ~ O(n) | Space: O(n)
class Solution:
    def findRedundantConnection(self, edges):
        parent = list(range(len(edges) + 1))
        rank = [0] * (len(edges) + 1)
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        for u, v in edges:
            pu, pv = find(u), find(v)
            if pu == pv: return [u, v]  # Already connected = redundant
            if rank[pu] < rank[pv]: parent[pu] = pv
            elif rank[pu] > rank[pv]: parent[pv] = pu
            else: parent[pv] = pu; rank[pu] += 1
