# Leetcode Link: https://leetcode.com/problems/time-based-key-value-store/
# **************** Python Solution ***********************
# ---------- Question ----------
# Store (key, value, timestamp) triples. get(key, timestamp) returns value with largest
# timestamp <= given timestamp.
# ---------- Approach ----------
# Hash map + binary search: store values with timestamps sorted, binary search for the
# largest timestamp <= query.
# Time: O(1) for set, O(log n) for get | Space: O(n)
from collections import defaultdict
class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))
    def get(self, key: str, timestamp: int) -> str:
        values = self.store[key]
        left, right = 0, len(values) - 1
        result = ""
        while left <= right:
            mid = (left + right) // 2
            if values[mid][0] <= timestamp:
                result = values[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        return result
