# Leetcode Link: https://leetcode.com/problems/word-search-ii/
# **************** Python Solution ***********************
# ---------- Question ----------
# Given an m x n board of characters and a list of words, return all words that can be found
# on the board. Words are constructed from adjacent cells (horizontally or vertically).
# ---------- Approach ----------
# Trie + DFS Backtracking: build a Trie of all target words, then DFS from each cell.
# When we reach a Trie leaf (word end), add the word to results.
# Time: O(m*n * 4^L * W) | Space: O(total chars in words)
class Solution:
    def findWords(self, board, words):
        root = {}
        for word in words:
            node = root
            for c in word:
                node = node.setdefault(c, {})
            node['#'] = word
        rows, cols = len(board), len(board[0])
        result = []
        def dfs(r, c, node):
            if '#' in node:
                result.append(node['#'])
                del node['#']  # Avoid duplicates
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            char = board[r][c]
            if char not in node:
                return
            board[r][c] = '.'  # Mark visited
            for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
                dfs(r+dr, c+dc, node[char])
            board[r][c] = char  # Restore
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)
        return result
