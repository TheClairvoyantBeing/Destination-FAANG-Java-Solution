# Leetcode Link: https://leetcode.com/problems/minimum-window-substring/

# **************** Python Solution ***********************

# ---------- Question ----------
# Given two strings s and t, return the minimum window substring of s that contains
# all characters of t (including duplicates). Return "" if no such window exists.
#
# Example:
#   Input: s = "ADOBECODEBANC", t = "ABC"
#   Output: "BANC"

# ---------- Approach ----------
# Sliding Window — expand right to include characters, shrink left when all
# characters of t are covered. Track character frequencies with counters.
#
# Time Complexity : O(|s| + |t|)
# Space Complexity: O(|s| + |t|) — for the frequency maps

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        t_count = Counter(t)          # Required character frequencies
        required = len(t_count)       # Number of unique characters needed
        formed = 0                    # How many unique chars have met their required count
        window_counts = {}

        ans = (float('inf'), None, None)  # (window_length, left, right)
        left = 0

        for right in range(len(s)):
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1

            # Check if this character's frequency requirement is met
            if char in t_count and window_counts[char] == t_count[char]:
                formed += 1

            # Try to shrink the window from the left
            while left <= right and formed == required:
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)

                left_char = s[left]
                window_counts[left_char] -= 1
                if left_char in t_count and window_counts[left_char] < t_count[left_char]:
                    formed -= 1
                left += 1

        return "" if ans[0] == float('inf') else s[ans[1]:ans[2] + 1]
