# Leetcode Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# **************** Python Solution ***********************
# ---------- Question ----------
# Find the minimum element in a rotated sorted array (no duplicates).
# Example: nums=[3,4,5,1,2] -> 1
# ---------- Approach ----------
# Binary search — if mid > right, minimum is in the right half; otherwise, it's in the left half.
# Time: O(log n) | Space: O(1)
class Solution:
    def findMin(self, nums) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1   # Min is in right half
            else:
                right = mid      # Min is in left half (including mid)
        return nums[left]
