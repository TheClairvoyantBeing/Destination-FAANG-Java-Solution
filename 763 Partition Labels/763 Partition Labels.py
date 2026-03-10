# Leetcode Link: https://leetcode.com/problems/partition-labels/
# **************** Python Solution ***********************
# ---------- Question ----------
# Partition string so each letter appears in at most one part. Maximize number of parts.
# Example: s="ababcbacadefegdehijhklij" -> [9,7,8]
# ---------- Approach ----------
# Record last occurrence of each character. Extend partition end to include all occurrences
# of characters in the current partition.
# Time: O(n) | Space: O(1) — at most 26 chars
class Solution:
    def partitionLabels(self, s: str):
        last = {c: i for i, c in enumerate(s)}  # Last index of each char
        result = []
        start = end = 0
        for i, c in enumerate(s):
            end = max(end, last[c])  # Extend partition to include all of c
            if i == end:             # Reached the end of current partition
                result.append(end - start + 1)
                start = end + 1
        return result
