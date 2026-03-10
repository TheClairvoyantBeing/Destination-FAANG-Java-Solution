# Leetcode Link: https://leetcode.com/problems/permutation-in-string/
# **************** Python Solution ***********************
# ---------- Question ----------
# Given s1 and s2, return true if s2 contains a permutation of s1.
# Example: s1="ab", s2="eidbaooo" -> True ("ba" is a permutation of "ab")
# ---------- Approach ----------
# Sliding window of size len(s1) over s2. Compare character frequency counters.
# Time: O(n) | Space: O(1) — at most 26 chars
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        s1_count = Counter(s1)
        window = Counter(s2[:len(s1)])
        if s1_count == window: return True
        for i in range(len(s1), len(s2)):
            window[s2[i]] += 1
            left_char = s2[i - len(s1)]
            window[left_char] -= 1
            if window[left_char] == 0: del window[left_char]
            if s1_count == window: return True
        return False
