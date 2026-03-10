# Leetcode Link: https://leetcode.com/problems/open-the-lock/
# **************** Python Solution ***********************
# ---------- Question ----------
# 4-wheel lock starts at "0000". Each move turns one wheel by one slot. Some combinations
# are deadends. Find minimum turns to reach target, or -1 if impossible.
# ---------- Approach ----------
# BFS from "0000": each state has 8 neighbors (4 wheels x 2 directions).
# Time: O(10^4 * 4) | Space: O(10^4)
from collections import deque
class Solution:
    def openLock(self, deadends, target: str) -> int:
        dead = set(deadends)
        if "0000" in dead: return -1
        queue = deque([("0000", 0)])
        visited = {"0000"}
        while queue:
            state, turns = queue.popleft()
            if state == target: return turns
            for i in range(4):
                digit = int(state[i])
                for d in (-1, 1):
                    new_digit = (digit + d) % 10
                    new_state = state[:i] + str(new_digit) + state[i+1:]
                    if new_state not in visited and new_state not in dead:
                        visited.add(new_state)
                        queue.append((new_state, turns + 1))
        return -1
