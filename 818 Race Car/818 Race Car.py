# Leetcode Link: https://leetcode.com/problems/race-car/
# **************** Python Solution ***********************
# ---------- Question ----------
# Car at position 0, speed 1. Instructions: A (accelerate: pos += speed, speed *= 2)
# or R (reverse: speed = -1 if positive, 1 if negative). Minimum instructions to reach target.
# ---------- Approach ----------
# BFS on states (position, speed). Explore A and R moves. Bound position to reasonable range.
# Time: O(target * log(target)) | Space: O(target * log(target))
from collections import deque
class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0, 1, 0)])
        visited = {(0, 1)}
        while queue:
            pos, speed, moves = queue.popleft()
            if pos == target: return moves
            # Accelerate
            npos, nspeed = pos + speed, speed * 2
            if (npos, nspeed) not in visited and 0 < npos < 2 * target:
                visited.add((npos, nspeed))
                queue.append((npos, nspeed, moves + 1))
            # Reverse
            nspeed = -1 if speed > 0 else 1
            if (pos, nspeed) not in visited:
                visited.add((pos, nspeed))
                queue.append((pos, nspeed, moves + 1))
        return -1
