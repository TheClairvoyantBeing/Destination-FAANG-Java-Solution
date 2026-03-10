# Leetcode Link: https://leetcode.com/problems/valid-parentheses/

# **************** Python Solution ***********************

# ---------- Question ----------
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
# An input string is valid if:
#   1. Open brackets are closed by the same type of brackets.
#   2. Open brackets are closed in the correct order.
#
# Example:
#   Input: s = "()[]{}"  ->  Output: True
#   Input: s = "(]"      ->  Output: False

# ---------- Approach ----------
# Use a stack — push opening brackets, pop when a closing bracket is encountered
# and check if it matches the top of the stack.
#
# Time Complexity : O(n) — single pass
# Space Complexity: O(n) — worst case all opening brackets

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}  # Closing -> Opening

        for char in s:
            if char in mapping:  # It's a closing bracket
                top = stack.pop() if stack else '#'
                if mapping[char] != top:
                    return False
            else:
                stack.append(char)  # It's an opening bracket

        return len(stack) == 0  # Valid only if all brackets were matched
