# Leetcode Link: https://leetcode.com/problems/valid-anagram/
# **************** Python Solution ***********************
# ---------- Question ----------
# Given two strings s and t, return true if t is an anagram of s.
# Example: s="anagram", t="nagaram" -> True
# ---------- Approach ----------
# Count character frequencies. Increment for s, decrement for t. If any count goes negative, false.
# Time: O(n) | Space: O(1) — fixed 26 lowercase letters
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1
        for c in t:
            count[c] = count.get(c, 0) - 1
            if count[c] < 0:
                return False
        return True
