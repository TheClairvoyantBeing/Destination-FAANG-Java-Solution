# Most asked problems at FAANG companies: https://docs.google.com/spreadsheets/d/1hzP8j7matoUiJ15N-RhsL5Dmig8_E3aP/edit#gid=1377915986
# Leetcode Link: https://leetcode.com/problems/evaluate-reverse-polish-notation/
# Video Solution: https://www.youtube.com/watch?v=vDRZN5i4b8U
# **************** Python Solution ***********************
# ---------- Question ----------
# Evaluate the value of an arithmetic expression in Reverse Polish Notation (postfix).
# Example: tokens=["2","1","+","3","*"] -> 9 ((2+1)*3)
# ---------- Approach ----------
# Stack — push numbers, pop two operands when an operator is encountered, push result.
# Note: Python's // truncates toward negative infinity; use int(a/b) for truncation toward zero.
# Time: O(n) | Space: O(n)
class Solution:
    def evalRPN(self, tokens) -> int:
        stack = []
        ops = {'+', '-', '*', '/'}
        for token in tokens:
            if token in ops:
                b = stack.pop()  # Second operand (popped first)
                a = stack.pop()  # First operand
                if token == '+':   stack.append(a + b)
                elif token == '-': stack.append(a - b)
                elif token == '*': stack.append(a * b)
                elif token == '/': stack.append(int(a / b))  # Truncate toward zero
            else:
                stack.append(int(token))
        return stack.pop()
