# Leetcode Link: https://leetcode.com/problems/find-the-celebrity/
# **************** Python Solution ***********************
# ---------- Question ----------
# Among n people, a celebrity is known by everyone but knows no one. Find the celebrity or return -1.
# You have a knows(a, b) API. Minimize API calls.
# ---------- Approach ----------
# Two passes: 1) Find candidate — if A knows B, A can't be celebrity, move to B.
# 2) Verify candidate — check all other people know candidate AND candidate knows nobody.
# Time: O(n) | Space: O(1)
class Solution:
    def findCelebrity(self, n: int) -> int:
        candidate = 0
        for i in range(1, n):
            if knows(candidate, i):
                candidate = i  # candidate knows i, so candidate isn't celebrity
        for i in range(n):
            if i != candidate:
                if knows(candidate, i) or not knows(i, candidate):
                    return -1  # candidate knows someone or someone doesn't know candidate
        return candidate
