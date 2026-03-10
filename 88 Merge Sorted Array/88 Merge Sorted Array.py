# Leetcode Link: https://leetcode.com/problems/merge-sorted-array/

# **************** Python Solution ***********************

# ---------- Question ----------
# You are given two sorted arrays nums1 and nums2. Merge nums2 into nums1 as one
# sorted array. nums1 has enough space (size m+n) to hold the additional elements.
#
# Example:
#   Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
#   Output: [1,2,2,3,5,6]

# ---------- Approach ----------
# Three-pointer merge from the end — fill nums1 from the back to avoid overwriting
# elements. Compare the largest remaining elements from both arrays.
#
# Time Complexity : O(m + n) — single pass
# Space Complexity: O(1) — in-place

class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        i, j, k = m - 1, n - 1, m + n - 1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]  # Place larger element at the end
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
