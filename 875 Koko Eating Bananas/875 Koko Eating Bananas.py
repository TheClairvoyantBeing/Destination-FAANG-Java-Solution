# Leetcode Link: https://leetcode.com/problems/koko-eating-bananas/
# **************** Python Solution ***********************
# ---------- Question ----------
# Koko eats bananas at speed k per hour. Given piles and h hours, find minimum k.
# Example: piles=[3,6,7,11], h=8 -> 4
# ---------- Approach ----------
# Binary search on k (eating speed). For each k, check if she can finish in h hours.
# Time: O(n * log(max(piles))) | Space: O(1)
import math
class Solution:
    def minEatingSpeed(self, piles, h: int) -> int:
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            hours = sum(math.ceil(p / mid) for p in piles)
            if hours <= h: right = mid      # Can eat slower
            else: left = mid + 1            # Need to eat faster
        return left
