# Leetcode Link: https://leetcode.com/problems/word-search/

# **************** Python Solution ***********************

# ---------- Question ----------
# Given an m x n board of characters and a string word, return true if word exists
# in the grid. The word can be constructed from adjacent cells (horizontally or
# vertically). Each cell may only be used once.
#
# Example:
#   Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
#   Output: True

# ---------- Approach ----------
# DFS Backtracking — for each cell matching word[0], start a DFS exploring
# all 4 directions. Mark visited cells temporarily to avoid reuse.
#
# Time Complexity : O(m * n * 4^L) — L is the word length
# Space Complexity: O(L) — recursion depth

class Solution:
    def exist(self, board, word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True  # All characters matched
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i]:
                return False  # Out of bounds or character mismatch

            temp = board[r][c]
            board[r][c] = '#'  # Mark as visited

            found = (dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or
                     dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1))

            board[r][c] = temp  # Restore (backtrack)
            return found

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False
