# Leetcode Link: https://leetcode.com/problems/alien-dictionary/
# **************** Python Solution ***********************
# ---------- Question ----------
# Given sorted list of words in an alien language, derive the alphabetical order.
# Return "" if the order is invalid. Example: ["wrt","wrf","er","ett","rftt"] -> "wertf"
# ---------- Approach ----------
# Build a directed graph from adjacent word comparisons, then topological sort (BFS/Kahn's).
# Time: O(C) where C = total chars across all words | Space: O(1) — at most 26 chars
from collections import defaultdict, deque
class Solution:
    def alienOrder(self, words) -> str:
        adj = defaultdict(set)
        in_degree = {c: 0 for word in words for c in word}  # Initialize all chars
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""  # Invalid: "abc" before "ab"
            for j in range(min_len):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        in_degree[w2[j]] += 1
                    break  # Only first difference matters
        queue = deque(c for c in in_degree if in_degree[c] == 0)
        result = []
        while queue:
            c = queue.popleft()
            result.append(c)
            for neighbor in adj[c]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        return ''.join(result) if len(result) == len(in_degree) else ""
