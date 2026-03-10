# Leetcode Link: https://leetcode.com/problems/longest-valid-parentheses/

# **************** Python Solution ***********************

# ---------- Question ----------
# Given a string containing just '(' and ')', return the length of the longest
# valid (well-formed) parentheses substring.
#
# Example:
#   Input: s = "(()"   ->  Output: 2
#   Input: s = ")()())" ->  Output: 4

# ---------- Approach ----------
# Stack-based — push indices onto the stack. Start with -1 as a base.
# When we see ')', pop the stack:
#   - If stack is empty, push current index as new base
#   - Otherwise, the valid length is current index - stack top
#
# Time Complexity : O(n) — single pass
# Space Complexity: O(n) — stack

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # Base index for calculating valid length
        max_len = 0

        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)           # Push index of '('
            else:
                stack.pop()               # Match with a '('
                if not stack:
                    stack.append(i)       # New base — unmatched ')'
                else:
                    max_len = max(max_len, i - stack[-1])  # Valid length

        return max_len
