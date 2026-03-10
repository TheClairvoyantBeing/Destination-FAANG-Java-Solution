# Leetcode Link: https://leetcode.com/problems/valid-parenthesis-string/
# **************** Python Solution ***********************
# ---------- Question ----------
# Given string with '(', ')' and '*' (* can be '(', ')' or empty), check if it's valid.
# Example: "(*))" -> True
# ---------- Approach ----------
# Track range [low, high] of possible open bracket counts.
# '(' increases both, ')' decreases both, '*' widens the range.
# If high < 0, impossible. If low < 0, reset to 0 (can't have negative open brackets).
# Time: O(n) | Space: O(1)
class Solution:
    def checkValidString(self, s: str) -> bool:
        low = high = 0
        for c in s:
            if c == '(': low += 1; high += 1
            elif c == ')': low -= 1; high -= 1
            else: low -= 1; high += 1  # * can be (, ), or empty
            if high < 0: return False
            low = max(low, 0)
        return low == 0
