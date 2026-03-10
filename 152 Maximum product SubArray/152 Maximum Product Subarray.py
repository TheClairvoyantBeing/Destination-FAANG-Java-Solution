# Leetcode Link: https://leetcode.com/problems/maximum-product-subarray/
# **************** Python Solution ***********************
# ---------- Question ----------
# Given an integer array, find the contiguous subarray with the largest product.
# Example: nums=[2,3,-2,4] -> 6 (subarray [2,3])
# ---------- Approach ----------
# Track both current max AND current min (since a negative * negative = positive).
# At each element, the new max is max(n, cur_max*n, cur_min*n).
# Time: O(n) | Space: O(1)
class Solution:
    def maxProduct(self, nums) -> int:
        result = max(nums)
        cur_min, cur_max = 1, 1
        for n in nums:
            temp = cur_max * n
            cur_max = max(n * cur_max, n * cur_min, n)
            cur_min = min(temp, n * cur_min, n)
            result = max(result, cur_max)
        return result
