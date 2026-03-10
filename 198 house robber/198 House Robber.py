# Leetcode Link: https://leetcode.com/problems/house-robber/
# **************** Python Solution ***********************
# ---------- Question ----------
# Rob houses along a street. Can't rob two adjacent houses. Maximize total money.
# Example: nums=[1,2,3,1] -> 4 (rob houses 0 and 2)
# ---------- Approach ----------
# DP with O(1) space: at each house, max(rob this + prev2, skip this = prev1).
# Time: O(n) | Space: O(1)
class Solution:
    def rob(self, nums) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        prev2, prev1 = 0, 0  # prev2 = 2 houses ago, prev1 = previous house
        for num in nums:
            temp = max(prev1, prev2 + num)  # Rob this house or skip it
            prev2 = prev1
            prev1 = temp
        return prev1
