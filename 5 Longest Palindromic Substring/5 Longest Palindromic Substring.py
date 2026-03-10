# Leetcode Link: https://leetcode.com/problems/longest-palindromic-substring/

# **************** Python Solution ***********************

# ---------- Question ----------
# Given a string s, return the longest palindromic substring in s.
#
# Example:
#   Input: s = "babad"
#   Output: "bab" (or "aba")

# ---------- Approach ----------
# Expand Around Center — for each character (and each pair of characters), expand
# outward while the substring remains a palindrome. Track the longest found.
#
# Time Complexity : O(n^2) — expansion takes O(n) for each of O(n) centers
# Space Complexity: O(1) — only storing indices

class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""

        def expand(l, r):
            nonlocal result
            # Expand as long as characters match and indices are valid
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(result):
                    result = s[l:r + 1]
                l -= 1
                r += 1

        for i in range(len(s)):
            expand(i, i)      # Odd-length palindromes  (single center)
            expand(i, i + 1)  # Even-length palindromes (two-char center)

        return result
