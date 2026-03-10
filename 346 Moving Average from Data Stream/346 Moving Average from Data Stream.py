# Leetcode Link: https://leetcode.com/problems/moving-average-from-data-stream/
# **************** Python Solution ***********************
# ---------- Question ----------
# Given a stream of integers and window size, compute moving average of last 'size' values.
# ---------- Approach ----------
# Use a deque as sliding window. Maintain running total for O(1) average computation.
# Time: O(1) per next() | Space: O(size)
from collections import deque
class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        self.total = 0
    def next(self, val: int) -> float:
        self.queue.append(val)
        self.total += val
        if len(self.queue) > self.size:
            self.total -= self.queue.popleft()
        return self.total / len(self.queue)
