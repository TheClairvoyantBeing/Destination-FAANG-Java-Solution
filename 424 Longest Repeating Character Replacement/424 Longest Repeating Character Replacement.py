# Leetcode Link: https://leetcode.com/problems/longest-repeating-character-replacement/
# **************** Python Solution ***********************
# ---------- Question ----------
# Given string s and integer k, you can replace at most k characters. Find the length of
# the longest substring containing the same letter after replacements.
# Example: s="AABABBA", k=1 -> 4 ("AABA" -> "AAAA")
# ---------- Approach ----------
# Sliding window: window is valid if (window_size - max_frequency) <= k.
# When invalid, shrink from left.
# Time: O(n) | Space: O(1) — at most 26 chars
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = max_freq = result = 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_freq = max(max_freq, count[s[right]])
            while (right - left + 1) - max_freq > k:  # Too many replacements needed
                count[s[left]] -= 1
                left += 1
            result = max(result, right - left + 1)
        return result
