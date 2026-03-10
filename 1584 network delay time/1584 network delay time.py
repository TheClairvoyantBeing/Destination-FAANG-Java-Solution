# Most asked problems at FAANG companies: https://docs.google.com/spreadsheets/d/1hzP8j7matoUiJ15N-RhsL5Dmig8_E3aP/edit#gid=1377915986
# Leetcode Link: https://leetcode.com/problems/network-delay-time/
# Video Solution: https://www.youtube.com/watch?v=QKRRjz4KMuE
# **************** Python Solution ***********************
# ---------- Question ----------
# N network nodes, given directed weighted edges. Signal sent from node k.
# Return the time for all nodes to receive the signal, or -1 if impossible.
# ---------- Approach ----------
# Dijkstra's algorithm with min-heap. Find shortest path from k to all nodes.
# Answer = max shortest distance (all nodes must be reached).
# Time: O(E log V) | Space: O(V + E)
import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times, n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        distances = [float('inf')] * (n + 1)
        distances[k] = 0
        pq = [(0, k)]  # (distance, node)
        while pq:
            curr_dist, curr_node = heapq.heappop(pq)
            if curr_dist > distances[curr_node]:
                continue  # Already found a shorter path
            for next_node, weight in graph[curr_node]:
                next_dist = curr_dist + weight
                if next_dist < distances[next_node]:
                    distances[next_node] = next_dist
                    heapq.heappush(pq, (next_dist, next_node))
        max_dist = max(distances[1:])
        return max_dist if max_dist != float('inf') else -1
