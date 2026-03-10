# Leetcode Link: https://leetcode.com/problems/implement-queue-using-stacks/
# **************** Python Solution ***********************
# ---------- Question ----------
# Implement a FIFO queue using only two stacks.
# ---------- Approach ----------
# Two stacks: stack_in for pushing, stack_out for popping. Transfer from stack_in to
# stack_out (reversing order) only when stack_out is empty — amortized O(1) per operation.
# Time: O(1) amortized | Space: O(n)
class MyQueue:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []
    def push(self, x: int) -> None:
        self.stack_in.append(x)
    def pop(self) -> int:
        self._move()
        return self.stack_out.pop()
    def peek(self) -> int:
        self._move()
        return self.stack_out[-1]
    def empty(self) -> bool:
        return not self.stack_in and not self.stack_out
    def _move(self):
        if not self.stack_out:  # Only transfer when output stack is empty
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
