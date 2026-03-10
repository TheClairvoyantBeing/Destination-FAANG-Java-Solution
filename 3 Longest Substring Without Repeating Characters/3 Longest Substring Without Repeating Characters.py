# LeetCode Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Youtube Explaination: https://youtu.be/RMQ-gRQAY0o

# **************** Python Solution ***********************

# ---------- Question ----------
# Given a string s, find the length of the longest substring without repeating characters.
#
# Example:
#   Input: s = "abcabcbb"
#   Output: 3
#   Explanation: The answer is "abc", with the length of 3.

# ---------- Approach ----------
# Sliding Window technique using a set to track characters in the current window.
# Expand the right pointer; if a duplicate is found, shrink the window from the left
# until the duplicate is removed.
#
# Time Complexity : O(n) — each character is visited at most twice
# Space Complexity: O(min(n, m)) — where m is the size of the character set

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        char_set = set()   # Tracks characters in the current window
        left = 0           # Left boundary of the sliding window
        ans = 0            # Stores the maximum length found

        for right in range(len(s)):
            # Shrink window from left until we can add s[right]
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            ans = max(ans, right - left + 1)  # Update max length

        return ans
