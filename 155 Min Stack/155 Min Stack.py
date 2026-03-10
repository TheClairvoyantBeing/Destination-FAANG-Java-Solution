# Most asked problems at FAANG companies: https://docs.google.com/spreadsheets/d/1hzP8j7matoUiJ15N-RhsL5Dmig8_E3aP/edit#gid=1377915986
# Leetcode Link: https://leetcode.com/problems/min-stack/
# Video Solution: https://www.youtube.com/watch?v=To2iap-ac3g
# **************** Python Solution ***********************
# ---------- Question ----------
# Design a stack that supports push, pop, top, and retrieving the minimum element in O(1).
# ---------- Approach ----------
# Two stacks: main stack for values, min_stack stores the current minimum at each level.
# When pushing, record min(val, current_min) on min_stack.
# Time: O(1) for all operations | Space: O(n)
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(val)
    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return self.min_stack[-1]
