# Leetcode Link: https://leetcode.com/problems/word-break/
# **************** Python Solution ***********************
# ---------- Question ----------
# Given a string s and a dictionary wordDict, return true if s can be segmented into
# space-separated words from the dictionary. Example: s="leetcode", dict=["leet","code"] -> True
# ---------- Approach ----------
# DP: dp[i] = True if s[0..i-1] can be segmented. For each position i, check all
# previous positions j: if dp[j] is True and s[j:i] is in the dictionary, dp[i] = True.
# Time: O(n^2 * k) where k is max word length | Space: O(n)
class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        word_set = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True  # Empty string is segmentable
        for i in range(1, len(s) + 1):
            for j in range(i - 1, -1, -1):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break  # No need to check further
        return dp[len(s)]
