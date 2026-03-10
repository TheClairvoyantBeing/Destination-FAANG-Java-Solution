# Most asked problems at FAANG companies: https://docs.google.com/spreadsheets/d/1hzP8j7matoUiJ15N-RhsL5Dmig8_E3aP/edit#gid=1377915986
# Leetcode Link: https://leetcode.com/problems/lru-cache
# Video Solution: https://www.youtube.com/watch?v=VPq5dlxaeP8
# **************** Python Solution ***********************
# ---------- Question ----------
# Design a data structure for Least Recently Used (LRU) cache.
# get(key): return value or -1. put(key, value): insert/update, evict LRU if at capacity.
# Both operations must be O(1).
# ---------- Approach ----------
# OrderedDict maintains insertion order. On access, move to end (most recent).
# On eviction, pop from front (least recent).
# Time: O(1) for both get and put | Space: O(capacity)
from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)  # Mark as recently used
        return self.cache[key]
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # Evict least recently used
