# Leetcode Link: https://leetcode.com/problems/generate-parentheses/

# **************** Python Solution ***********************

# ---------- Question ----------
# Given n pairs of parentheses, generate all combinations of well-formed parentheses.
#
# Example:
#   Input: n = 3
#   Output: ["((()))","(()())","(())()","()(())","()()()"]

# ---------- Approach ----------
# Backtracking — build the string character by character:
#   - Add '(' if we haven't used all n open brackets
#   - Add ')' if it won't create an invalid sequence (close_count < open_count)
#
# Time Complexity : O(4^n / sqrt(n)) — the n-th Catalan number
# Space Complexity: O(n) — recursion depth

class Solution:
    def generateParenthesis(self, n: int):
        result = []

        def backtrack(s, open_count, close_count):
            if len(s) == 2 * n:     # Complete valid combination
                result.append(s)
                return
            if open_count < n:      # Can still add '('
                backtrack(s + '(', open_count + 1, close_count)
            if close_count < open_count:  # Can add ')' without invalidating
                backtrack(s + ')', open_count, close_count + 1)

        backtrack('', 0, 0)
        return result
