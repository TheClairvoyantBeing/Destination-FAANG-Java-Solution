# Leetcode Link: https://leetcode.com/problems/majority-element/
# **************** Python Solution ***********************
# ---------- Question ----------
# Find the element that appears more than n/2 times. Guaranteed to exist.
# Example: nums=[2,2,1,1,1,2,2] -> 2
# ---------- Approach ----------
# Boyer-Moore Voting Algorithm: maintain a candidate and count. When count=0, pick new candidate.
# Increment count for same element, decrement for different. Majority element survives.
# Time: O(n) | Space: O(1)
class Solution:
    def majorityElement(self, nums) -> int:
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        return candidate
