# Leetcode Link: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
# **************** Python Solution ***********************
# ---------- Question ----------
# Remove the minimum number of parentheses so that the resulting string is valid.
# Example: s="lee(t(c)o)de)" -> "lee(t(c)o)de"
# ---------- Approach ----------
# Two-pass with stack: first identify indices of unmatched parentheses, then build
# the result string excluding those indices.
# Time: O(n) | Space: O(n)
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        indexes_to_remove = set()
        stack = []  # Stack of indices of unmatched '('
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if stack:
                    stack.pop()           # Matched with a '('
                else:
                    indexes_to_remove.add(i)  # Unmatched ')'
        indexes_to_remove = indexes_to_remove.union(set(stack))  # Add unmatched '('
        return ''.join(c for i, c in enumerate(s) if i not in indexes_to_remove)
