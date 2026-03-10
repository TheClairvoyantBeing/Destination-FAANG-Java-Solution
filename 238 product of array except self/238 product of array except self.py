# Leetcode Link: https://leetcode.com/problems/product-of-array-except-self/
# **************** Python Solution ***********************
# ---------- Question ----------
# Given array nums, return array where answer[i] is the product of all elements except nums[i].
# Must run in O(n) without using division. Example: [1,2,3,4] -> [24,12,8,6]
# ---------- Approach ----------
# Two-pass: first pass computes prefix products (left to right),
# second pass multiplies by postfix products (right to left).
# Time: O(n) | Space: O(1) — output array doesn't count as extra space
class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        result = [1] * n
        prefix = 1
        for i in range(n):       # Left-to-right: prefix products
            result[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(n - 1, -1, -1):  # Right-to-left: multiply by postfix
            result[i] *= postfix
            postfix *= nums[i]
        return result
