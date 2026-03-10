# Leetcode Link: https://leetcode.com/problems/largest-number/
# **************** Python Solution ***********************
# ---------- Question ----------
# Given a list of non-negative integers, arrange them to form the largest number.
# Example: nums=[10,2] -> "210"
# ---------- Approach ----------
# Custom sort: compare by concatenation order. "9" vs "34": "934" > "349", so "9" comes first.
# Time: O(n log n * k) where k is average digit count | Space: O(n)
from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums) -> str:
        def compare(x, y):
            if x + y > y + x: return -1   # x should come before y
            elif x + y < y + x: return 1  # y should come before x
            else: return 0
        nums = [str(n) for n in nums]
        nums.sort(key=cmp_to_key(compare))
        result = ''.join(nums)
        return '0' if result[0] == '0' else result  # Handle all-zeros case
