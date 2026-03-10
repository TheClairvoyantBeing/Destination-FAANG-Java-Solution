# Leetcode Link: https://leetcode.com/problems/car-fleet/
# **************** Python Solution ***********************
# ---------- Question ----------
# Cars at various positions heading to target at various speeds. Slower car blocks faster one.
# Count number of car fleets that arrive at target.
# ---------- Approach ----------
# Sort by position (descending). Calculate time to reach target. If a car takes longer
# than the one ahead, it forms a new fleet.
# Time: O(n log n) | Space: O(n)
class Solution:
    def carFleet(self, target: int, position, speed) -> int:
        pairs = sorted(zip(position, speed), reverse=True)
        stack = []
        for pos, spd in pairs:
            time = (target - pos) / spd
            if not stack or time > stack[-1]:
                stack.append(time)  # New fleet
        return len(stack)
