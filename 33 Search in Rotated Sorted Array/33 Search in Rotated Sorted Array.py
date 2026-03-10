# Leetcode Link: https://leetcode.com/problems/search-in-rotated-sorted-array/

# **************** Python Solution ***********************

# ---------- Question ----------
# You are given a sorted array that has been rotated at an unknown pivot.
# Given a target value, return its index, or -1 if not found.
# You must write an algorithm with O(log n) runtime complexity.
#
# Example:
#   Input: nums = [4,5,6,7,0,1,2], target = 0  ->  Output: 4

# ---------- Approach ----------
# Modified Binary Search — at each step, determine which half is sorted,
# then check if the target falls within that sorted half.
#
# Time Complexity : O(log n)
# Space Complexity: O(1)

class Solution:
    def search(self, nums, target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            # Left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # Target is in left sorted half
                else:
                    left = mid + 1   # Target is in right half
            # Right half is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1   # Target is in right sorted half
                else:
                    right = mid - 1  # Target is in left half

        return -1
