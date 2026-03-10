# Leetcode Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# **************** Python Solution ***********************
# ---------- Question ----------
# Given a 1-indexed sorted array, find two numbers that add up to target. Return their indices.
# Example: numbers=[2,7,11,15], target=9 -> [1,2]
# ---------- Approach ----------
# Two pointers: if sum < target, move left pointer right; if sum > target, move right pointer left.
# Time: O(n) | Space: O(1)
class Solution:
    def twoSum(self, numbers, target: int):
        left, right = 0, len(numbers) - 1
        while left < right:
            s = numbers[left] + numbers[right]
            if s == target:
                return [left + 1, right + 1]  # 1-indexed
            elif s < target:
                left += 1
            else:
                right -= 1
        return [-1, -1]
