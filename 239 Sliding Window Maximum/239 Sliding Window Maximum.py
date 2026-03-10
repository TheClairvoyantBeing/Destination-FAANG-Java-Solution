# Leetcode Link: https://leetcode.com/problems/sliding-window-maximum/
# **************** Python Solution ***********************
# ---------- Question ----------
# Given array nums and window size k, return the maximum in each sliding window.
# Example: nums=[1,3,-1,-3,5,3,6,7], k=3 -> [3,3,5,5,6,7]
# ---------- Approach ----------
# Monotonic decreasing deque: front always holds the index of the max in the current window.
# Remove indices outside the window from front, remove smaller elements from back.
# Time: O(n) | Space: O(k)
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k: int):
        result = []
        dq = deque()  # Stores indices
        for i in range(len(nums)):
            while dq and dq[0] < i - k + 1:   # Remove out-of-window indices
                dq.popleft()
            while dq and nums[dq[-1]] < nums[i]:  # Maintain decreasing order
                dq.pop()
            dq.append(i)
            if i >= k - 1:  # Window is fully formed
                result.append(nums[dq[0]])
        return result
