# Leetcode Link: https://leetcode.com/problems/insert-delete-getrandom-o1/
# **************** Python Solution ***********************
# ---------- Question ----------
# Design a data structure: insert, remove, getRandom — all average O(1).
# ---------- Approach ----------
# List + HashMap: list stores values, map stores value->index.
# On remove: swap target with last element (O(1) list removal from end).
# Time: O(1) average for all ops | Space: O(n)
import random
class RandomizedSet:
    def __init__(self):
        self.val_to_idx = {}
        self.vals = []
    def insert(self, val: int) -> bool:
        if val in self.val_to_idx: return False
        self.val_to_idx[val] = len(self.vals)
        self.vals.append(val)
        return True
    def remove(self, val: int) -> bool:
        if val not in self.val_to_idx: return False
        idx = self.val_to_idx[val]
        last_val = self.vals[-1]
        self.vals[idx] = last_val           # Swap with last
        self.val_to_idx[last_val] = idx
        self.vals.pop()
        del self.val_to_idx[val]
        return True
    def getRandom(self) -> int:
        return random.choice(self.vals)
