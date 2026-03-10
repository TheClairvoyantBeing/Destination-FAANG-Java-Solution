# Leetcode Link: https://leetcode.com/problems/next-permutation/

# **************** Python Solution ***********************

# ---------- Question ----------
# Implement next permutation, which rearranges numbers into the lexicographically
# next greater permutation. If no such arrangement exists, rearrange to the lowest
# possible order (i.e., sorted in ascending order). Must be done in-place.
#
# Example:
#   Input: nums = [1,2,3]  ->  Output: [1,3,2]
#   Input: nums = [3,2,1]  ->  Output: [1,2,3]

# ---------- Approach ----------
# 1. Find the largest index i such that nums[i] < nums[i+1] (first decreasing element from right)
# 2. Find the largest index j > i such that nums[j] > nums[i]
# 3. Swap nums[i] and nums[j]
# 4. Reverse the suffix after index i
#
# Time Complexity : O(n)
# Space Complexity: O(1)

class Solution:
    def nextPermutation(self, nums) -> None:
        n = len(nums)
        i = n - 2

        # Step 1: Find first element smaller than its next (from right)
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            # Step 2: Find the smallest element larger than nums[i] (from right)
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            # Step 3: Swap
            nums[i], nums[j] = nums[j], nums[i]

        # Step 4: Reverse the suffix starting at i+1
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
