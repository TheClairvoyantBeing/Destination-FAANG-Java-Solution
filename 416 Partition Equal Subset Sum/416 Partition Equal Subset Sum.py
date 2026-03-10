# Leetcode Link: https://leetcode.com/problems/partition-equal-subset-sum/
# **************** Python Solution ***********************
# ---------- Question ----------
# Given array, determine if it can be partitioned into two subsets with equal sum.
# Example: nums=[1,5,11,5] -> True ([1,5,5] and [11])
# ---------- Approach ----------
# DP subset sum: can we make sum = total/2? Use a set of achievable sums.
# Time: O(n * sum) | Space: O(sum)
class Solution:
    def canPartition(self, nums) -> bool:
        total = sum(nums)
        if total % 2 != 0: return False
        target = total // 2
        dp = set([0])
        for num in nums:
            new_dp = set()
            for t in dp:
                if t + num == target: return True
                new_dp.add(t + num)
            dp.update(new_dp)
        return target in dp
