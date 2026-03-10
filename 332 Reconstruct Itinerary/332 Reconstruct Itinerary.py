# Leetcode Link: https://leetcode.com/problems/reconstruct-itinerary/
# **************** Python Solution ***********************
# ---------- Question ----------
# Given airline tickets, reconstruct the itinerary starting from "JFK" in lexical order.
# Example: tickets=[["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# -> ["JFK","ATL","JFK","SFO","ATL","SFO"]
# ---------- Approach ----------
# Hierholzer's algorithm for Eulerian path. Build adjacency list sorted in reverse,
# DFS post-order traversal, reverse at end.
# Time: O(E log E) for sorting | Space: O(E)
from collections import defaultdict
class Solution:
    def findItinerary(self, tickets):
        graph = defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)
        route = []
        def dfs(airport):
            while graph[airport]:
                dfs(graph[airport].pop())
            route.append(airport)
        dfs("JFK")
        return route[::-1]
