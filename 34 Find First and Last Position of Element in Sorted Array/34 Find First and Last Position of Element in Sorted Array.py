# Leetcode Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

# **************** Python Solution ***********************

# ---------- Question ----------
# Given an array of integers sorted in non-decreasing order, find the starting
# and ending position of a given target value. Return [-1, -1] if not found.
# Must run in O(log n) time.
#
# Example:
#   Input: nums = [5,7,7,8,8,10], target = 8  ->  Output: [3, 4]

# ---------- Approach ----------
# Two binary searches — one to find the first occurrence (bias left) and one
# to find the last occurrence (bias right).
#
# Time Complexity : O(log n)
# Space Complexity: O(1)

class Solution:
    def searchRange(self, nums, target: int):
        def findFirst():
            left, right = 0, len(nums) - 1
            result = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    result = mid
                    right = mid - 1  # Keep searching left for first occurrence
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return result

        def findLast():
            left, right = 0, len(nums) - 1
            result = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    result = mid
                    left = mid + 1  # Keep searching right for last occurrence
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return result

        return [findFirst(), findLast()]
