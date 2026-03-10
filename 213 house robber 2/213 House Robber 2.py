# Leetcode Link: https://leetcode.com/problems/house-robber-ii/
# **************** Python Solution ***********************
# ---------- Question ----------
# Houses are arranged in a circle. Can't rob two adjacent houses. Maximize total money.
# Example: nums=[2,3,2] -> 3 (rob house 1 only)
# ---------- Approach ----------
# Since first and last are adjacent, run House Robber I on two subarrays:
# nums[0..n-2] and nums[1..n-1]. Take the max.
# Time: O(n) | Space: O(1)
class Solution:
    def rob(self, nums) -> int:
        if len(nums) == 1: return nums[0]
        def rob_linear(houses):
            prev2, prev1 = 0, 0
            for h in houses:
                prev2, prev1 = prev1, max(prev1, prev2 + h)
            return prev1
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
