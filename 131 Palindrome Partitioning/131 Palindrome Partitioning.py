# Leetcode Link: https://leetcode.com/problems/palindrome-partitioning/
# **************** Python Solution ***********************
# ---------- Question ----------
# Given a string s, partition it so every substring is a palindrome. Return all possible partitions.
# Example: s="aab" -> [["a","a","b"],["aa","b"]]
# ---------- Approach ----------
# Backtracking — at each position, try all substrings starting from that position.
# If the substring is a palindrome, add it and recurse on the remaining string.
# Time: O(n * 2^n) | Space: O(n)
class Solution:
    def partition(self, s: str):
        result = []
        def backtrack(start, path):
            if start == len(s):
                result.append(path[:])
                return
            for end in range(start + 1, len(s) + 1):
                sub = s[start:end]
                if sub == sub[::-1]:           # Check palindrome
                    path.append(sub)
                    backtrack(end, path)
                    path.pop()                 # Backtrack
        backtrack(0, [])
        return result
