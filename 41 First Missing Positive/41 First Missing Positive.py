# Leetcode Link: https://leetcode.com/problems/first-missing-positive/

# **************** Python Solution ***********************

# ---------- Question ----------
# Given an unsorted integer array nums, return the smallest missing positive integer.
# Must run in O(n) time and use O(1) auxiliary space.
#
# Example:
#   Input: nums = [3,4,-1,1]  ->  Output: 2
#   Input: nums = [1,2,0]     ->  Output: 3

# ---------- Approach ----------
# Cyclic Sort — place each number at its "correct" index (nums[i] should hold i+1).
# After sorting, the first index where nums[i] != i+1 gives the answer.
#
# Time Complexity : O(n) — each element is swapped at most once
# Space Complexity: O(1) — in-place

class Solution:
    def firstMissingPositive(self, nums) -> int:
        n = len(nums)

        # Place each number in its correct position: nums[i] should be i+1
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap nums[i] to its correct position
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        # Find the first position where nums[i] != i+1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1  # All positions 1..n are filled
