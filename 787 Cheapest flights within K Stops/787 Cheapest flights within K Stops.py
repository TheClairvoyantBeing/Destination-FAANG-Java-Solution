# Leetcode Link: https://leetcode.com/problems/cheapest-flights-within-k-stops/
# **************** Python Solution ***********************
# ---------- Question ----------
# Find cheapest flight from src to dst with at most k stops. Return -1 if impossible.
# ---------- Approach ----------
# Bellman-Ford (k+1 iterations): relax all edges k+1 times. Use temp copy to avoid
# using updates from the same iteration.
# Time: O(k * E) | Space: O(V)
class Solution:
    def findCheapestPrice(self, n: int, flights, src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0
        for _ in range(k + 1):
            temp = prices[:]
            for u, v, w in flights:
                if prices[u] != float('inf') and prices[u] + w < temp[v]:
                    temp[v] = prices[u] + w
            prices = temp
        return prices[dst] if prices[dst] != float('inf') else -1
