# Most asked problems at FAANG companies: https://docs.google.com/spreadsheets/d/1hzP8j7matoUiJ15N-RhsL5Dmig8_E3aP/edit#gid=1377915986
# Leetcode Link: https://leetcode.com/problems/longest-common-prefix/
# Video Solution: https://www.youtube.com/watch?v=PWoIZxcamsQ

# **************** Python Solution ***********************

# ---------- Question ----------
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return "".
#
# Example:
#   Input: strs = ["flower", "flow", "flight"]
#   Output: "fl"

# ---------- Approach ----------
# Start with the first string as the prefix. For each subsequent string, shorten the
# prefix until it matches the beginning of that string.
#
# Time Complexity : O(S) — where S is the sum of all characters in all strings
# Space Complexity: O(1)

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if not strs:
            return ""

        prefix = strs[0]  # Start with the first string as prefix
        for s in strs[1:]:
            # Shrink prefix until it matches the start of s
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
