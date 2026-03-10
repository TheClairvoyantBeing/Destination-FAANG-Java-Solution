# Leetcode Link: https://leetcode.com/problems/word-ladder/
# **************** Python Solution ***********************
# ---------- Question ----------
# Given beginWord, endWord, and a wordList, find the shortest transformation sequence
# from beginWord to endWord where each step changes exactly one letter.
# Example: beginWord="hit", endWord="cog", wordList=["hot","dot","dog","lot","log","cog"] -> 5
# ---------- Approach ----------
# BFS — each word is a node, edges connect words differing by one letter. BFS finds shortest path.
# Time: O(M^2 * N) — M=word length, N=wordList size | Space: O(M^2 * N)
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        queue = deque([(beginWord, 1)])  # (current word, steps)
        visited = {beginWord}
        while queue:
            word, length = queue.popleft()
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i + 1:]
                    if next_word == endWord:
                        return length + 1
                    if next_word in word_set and next_word not in visited:
                        visited.add(next_word)
                        queue.append((next_word, length + 1))
        return 0
