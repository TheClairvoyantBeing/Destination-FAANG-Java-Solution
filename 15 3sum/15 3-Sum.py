# Best Leetcode problems for FAANG: https://docs.google.com/spreadsheets/d/1hzP8j7matoUiJ15N-RhsL5Dmig8_E3aP/edit#gid=1377915986
# Video Solution: https://www.youtube.com/watch?v=WtloSzFYvho
# Leetcode Link: https://leetcode.com/problems/3sum/

# **************** Python Solution ***********************

# ---------- Question ----------
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# The solution set must not contain duplicate triplets.
#
# Example:
#   Input: nums = [-1, 0, 1, 2, -1, -4]
#   Output: [[-1, -1, 2], [-1, 0, 1]]

# ---------- Approach ----------
# Sort + Two Pointers — fix one element, then use two pointers on the remaining
# sorted portion. Skip duplicates to avoid repeated triplets.
#
# Time Complexity : O(n^2)
# Space Complexity: O(1) — ignoring the output list

class Solution:
    def threeSum(self, nums):
        nums.sort()
        result = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break  # Since array is sorted, no three positives can sum to 0
            if i == 0 or nums[i] != nums[i - 1]:  # Skip duplicate values for i
                left, right = i + 1, len(nums) - 1
                while left < right:
                    s = nums[i] + nums[left] + nums[right]
                    if s < 0:
                        left += 1        # Need a larger sum
                    elif s > 0:
                        right -= 1       # Need a smaller sum
                    else:
                        result.append([nums[i], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        # Skip duplicate values for left pointer
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1

        return result
