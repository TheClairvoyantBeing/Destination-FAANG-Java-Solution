# Leetcode Link: https://leetcode.com/problems/group-anagrams/

# **************** Python Solution ***********************

# ---------- Question ----------
# Given an array of strings, group the anagrams together. An anagram is a word
# formed by rearranging the letters of a different word using all original letters.
#
# Example:
#   Input: strs = ["eat","tea","tan","ate","nat","bat"]
#   Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# ---------- Approach ----------
# Hash map with sorted string as key — anagrams will have the same sorted form.
# Group strings by their sorted character version.
#
# Time Complexity : O(n * k log k) — n strings, each of length k sorted
# Space Complexity: O(n * k) — storing all strings in the hash map

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        groups = defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))  # Sorted chars as the grouping key
            groups[key].append(s)
        return list(groups.values())
