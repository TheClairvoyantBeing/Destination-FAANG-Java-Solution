# Leetcode Link: https://leetcode.com/problems/find-the-duplicate-number/
# **************** Python Solution ***********************
# ---------- Question ----------
# Array of n+1 integers in range [1, n]. Exactly one number is repeated.
# Find the duplicate without modifying the array. Must use O(1) space.
# Example: nums=[1,3,4,2,2] -> 2
# ---------- Approach ----------
# Floyd's Cycle Detection: treat the array like a linked list (nums[i] points to next index).
# A cycle exists because of the duplicate. Find the cycle, then find its entry point.
# Time: O(n) | Space: O(1)
class Solution:
    def findDuplicate(self, nums) -> int:
        slow = nums[0]
        fast = nums[0]
        while True:                     # Detect cycle
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: break
        slow = nums[0]                  # Find entry point
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
