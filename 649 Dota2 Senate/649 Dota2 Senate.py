# Leetcode Link: https://leetcode.com/problems/dota2-senate/
# **************** Python Solution ***********************
# ---------- Question ----------
# Senate votes to ban the other party. Each senator can ban one senator from the opposing party
# (bans the nearest future opponent). Which party wins? Return "Radiant" or "Dire".
# ---------- Approach ----------
# Two queues: one for each party. Compare front of each queue — smaller index bans the other
# and goes to the back (index + n to simulate next round).
# Time: O(n) | Space: O(n)
from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant, dire = deque(), deque()
        n = len(senate)
        for i, c in enumerate(senate):
            if c == 'R': radiant.append(i)
            else: dire.append(i)
        while radiant and dire:
            r, d = radiant.popleft(), dire.popleft()
            if r < d: radiant.append(r + n)  # Radiant bans Dire, goes to next round
            else: dire.append(d + n)
        return "Radiant" if radiant else "Dire"
