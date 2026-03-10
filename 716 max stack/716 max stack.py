# Leetcode Link: https://leetcode.com/problems/max-stack/
# **************** Python Solution ***********************
# ---------- Question ----------
# Design a max stack: push, pop, top, peekMax, popMax (remove and return max element).
# ---------- Approach ----------
# Two stacks: main stack and max-tracking stack. popMax uses temp buffer to find and remove max.
# Time: O(1) for push/pop/top/peekMax, O(n) for popMax | Space: O(n)
class MaxStack:
    def __init__(self):
        self.stack = []
        self.max_stack = []
    def push(self, x: int) -> None:
        self.stack.append(x)
        self.max_stack.append(x if not self.max_stack else max(x, self.max_stack[-1]))
    def pop(self) -> int:
        self.max_stack.pop()
        return self.stack.pop()
    def top(self) -> int:
        return self.stack[-1]
    def peekMax(self) -> int:
        return self.max_stack[-1]
    def popMax(self) -> int:
        max_val = self.max_stack[-1]
        temp = []
        while self.stack[-1] != max_val:
            temp.append(self.pop())
        self.pop()  # Remove the max element
        while temp:
            self.push(temp.pop())
        return max_val
