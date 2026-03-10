# Leetcode Link: https://leetcode.com/problems/number-of-provinces/
# **************** Python Solution ***********************
# ---------- Question ----------
# Given n x n adjacency matrix isConnected, return the number of provinces (connected components).
# ---------- Approach ----------
# DFS: for each unvisited city, DFS to visit all connected cities = one province.
# Time: O(n^2) | Space: O(n)
class Solution:
    def findCircleNum(self, isConnected) -> int:
        n = len(isConnected)
        visited = set()
        provinces = 0
        def dfs(city):
            for neighbor in range(n):
                if isConnected[city][neighbor] == 1 and neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)
        for city in range(n):
            if city not in visited:
                visited.add(city)
                dfs(city)
                provinces += 1
        return provinces
