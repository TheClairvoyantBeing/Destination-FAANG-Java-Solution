# Leetcode Link: https://leetcode.com/problems/single-number/
# **************** Python Solution ***********************
# ---------- Question ----------
# Given an array where every element appears twice except one, find that single element.
# Must use O(1) extra space. Example: nums=[4,1,2,1,2] -> 4
# ---------- Approach ----------
# XOR all elements: a ^ a = 0, a ^ 0 = a. All pairs cancel out, leaving the single number.
# Time: O(n) | Space: O(1)
class Solution:
    def singleNumber(self, nums) -> int:
        result = 0
        for num in nums:
            result ^= num  # XOR: pairs cancel out
        return result
