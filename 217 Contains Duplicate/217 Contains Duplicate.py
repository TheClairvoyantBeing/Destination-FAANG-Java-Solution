# Leetcode Link: https://leetcode.com/problems/contains-duplicate/
# **************** Python Solution ***********************
# ---------- Question ----------
# Return true if any value appears at least twice in the array.
# Example: nums=[1,2,3,1] -> True
# ---------- Approach ----------
# Convert to set and compare lengths. If set is smaller, there were duplicates.
# Time: O(n) | Space: O(n)
class Solution:
    def containsDuplicate(self, nums) -> bool:
        return len(nums) != len(set(nums))
