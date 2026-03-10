# Leetcode Link: https://leetcode.com/problems/verifying-an-alien-dictionary/
# **************** Python Solution ***********************
# ---------- Question ----------
# Given words and alien alphabet order, verify words are sorted lexicographically.
# Example: words=["hello","leetcode"], order="hlabcdefgijkmnopqrstuvwxyz" -> True
# ---------- Approach ----------
# Build order map, compare adjacent words character by character.
# Time: O(total chars) | Space: O(1) — 26-char map
class Solution:
    def isAlienSorted(self, words, order: str) -> bool:
        order_map = {c: i for i, c in enumerate(order)}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            for j in range(len(w1)):
                if j >= len(w2): return False  # "apple" > "app" in any order
                if w1[j] != w2[j]:
                    if order_map[w1[j]] > order_map[w2[j]]: return False
                    break
        return True
