# Leetcode Link: https://leetcode.com/problems/binary-search/
# **************** Python Solution ***********************
# ---------- Question ----------
# Given sorted array and target, return index of target or -1.
# ---------- Approach ----------
# Classic binary search: compare mid element, narrow to left or right half.
# Time: O(log n) | Space: O(1)
class Solution:
    def search(self, nums, target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target: return mid
            elif nums[mid] < target: left = mid + 1
            else: right = mid - 1
        return -1
