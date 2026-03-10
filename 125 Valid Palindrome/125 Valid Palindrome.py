# Leetcode Link: https://leetcode.com/problems/valid-palindrome/
# **************** Python Solution ***********************
# ---------- Question ----------
# Given a string, determine if it is a palindrome considering only alphanumeric characters
# and ignoring case. Example: "A man, a plan, a canal: Panama" -> True
# ---------- Approach ----------
# Two pointers from both ends, skip non-alphanumeric chars, compare case-insensitively.
# Time: O(n) | Space: O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1             # Skip non-alphanumeric from left
            while left < right and not s[right].isalnum():
                right -= 1           # Skip non-alphanumeric from right
            if s[left].lower() != s[right].lower():
                return False         # Mismatch found
            left += 1
            right -= 1
        return True
