# Leetcode Link: https://leetcode.com/problems/longest-increasing-subsequence/
# **************** Python Solution ***********************
# ---------- Question ----------
# Same as above but using O(n log n) approach with binary search.
# ---------- Approach ----------
# Patience Sorting: maintain an array of "tails" (smallest possible tail for LIS of each length).
# Use binary search (bisect_left) to find where each number should go.
# Time: O(n log n) | Space: O(n)
import bisect
class Solution:
    def lengthOfLIS(self, nums) -> int:
        tails = []
        for num in nums:
            pos = bisect.bisect_left(tails, num)
            if pos == len(tails):
                tails.append(num)   # Extends the longest subsequence
            else:
                tails[pos] = num     # Replace to keep smallest possible tail
        return len(tails)
