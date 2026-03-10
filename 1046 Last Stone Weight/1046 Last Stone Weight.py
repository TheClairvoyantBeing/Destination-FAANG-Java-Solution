# Leetcode Link: https://leetcode.com/problems/last-stone-weight/
# **************** Python Solution ***********************
# ---------- Question ----------
# Given array of stone weights. Each turn, smash two heaviest stones. If equal, both destroyed.
# If not, the lighter is destroyed and the heavier loses that weight. Return last stone weight or 0.
# Example: stones=[2,7,4,1,8,1] -> 1
# ---------- Approach ----------
# Max-heap (negate values since Python has min-heap). Pop two, push difference if non-zero.
# Time: O(n log n) | Space: O(n)
import heapq
class Solution:
    def lastStoneWeight(self, stones) -> int:
        stones = [-s for s in stones]  # Negate for max-heap
        heapq.heapify(stones)
        while len(stones) > 1:
            first = -heapq.heappop(stones)
            second = -heapq.heappop(stones)
            if first != second:
                heapq.heappush(stones, -(first - second))
        return -stones[0] if stones else 0
