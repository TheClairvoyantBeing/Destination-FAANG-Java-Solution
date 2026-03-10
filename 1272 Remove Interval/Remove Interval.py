# Leetcode Link: https://leetcode.com/problems/remove-interval/
# **************** Python Solution ***********************
# ---------- Question ----------
# Given sorted intervals and an interval toBeRemoved, return the remaining intervals
# after removing the overlap with toBeRemoved.
# Example: intervals=[[0,2],[3,4],[5,7]], toBeRemoved=[1,6] -> [[0,1],[6,7]]
# ---------- Approach ----------
# For each interval: if no overlap, keep it. If partial overlap, keep the non-overlapping parts.
# Time: O(n) | Space: O(n)
class Solution:
    def removeInterval(self, intervals, toBeRemoved):
        result = []
        remove_start, remove_end = toBeRemoved
        for start, end in intervals:
            if end <= remove_start or start >= remove_end:
                result.append([start, end])     # No overlap — keep as-is
            else:
                if start < remove_start:
                    result.append([start, remove_start])   # Left portion survives
                if end > remove_end:
                    result.append([remove_end, end])        # Right portion survives
        return result
