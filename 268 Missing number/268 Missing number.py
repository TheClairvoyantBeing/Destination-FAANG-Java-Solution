# Leetcode Link: https://leetcode.com/problems/missing-number/
# **************** Python Solution ***********************
# ---------- Question ----------
# Given array of n distinct numbers in range [0, n], find the missing one.
# Example: nums=[3,0,1] -> 2
# ---------- Approach ----------
# Math: sum(0..n) - sum(nums) = missing number.
# Time: O(n) | Space: O(1)
class Solution:
    def missingNumber(self, nums) -> int:
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)
