# Leetcode Link: https://leetcode.com/problems/median-of-two-sorted-arrays/

# **************** Python Solution ***********************

# ---------- Question ----------
# Given two sorted arrays nums1 and nums2 of size m and n respectively,
# return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).
#
# Example:
#   Input: nums1 = [1,3], nums2 = [2]
#   Output: 2.0
#   Explanation: The merged array = [1,2,3] and median is 2.

# ---------- Approach ----------
# Binary search on the smaller array to find the correct partition where:
#   - All elements on the left side <= all elements on the right side.
# This avoids merging the arrays, giving O(log(min(m, n))) time.
#
# Time Complexity : O(log(min(m, n)))
# Space Complexity: O(1)

class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A  # Ensure A is the shorter array

        total = len(A) + len(B)
        half = total // 2

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2          # Partition index for A
            j = half - i - 2          # Partition index for B

            # Edge values: use -inf / +inf when partition is at array boundary
            Aleft  = A[i]     if i >= 0          else float('-inf')
            Aright = A[i + 1] if (i + 1) < len(A) else float('inf')
            Bleft  = B[j]     if j >= 0          else float('-inf')
            Bright = B[j + 1] if (j + 1) < len(B) else float('inf')

            # Check if we found the correct partition
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:  # Odd total length
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1  # Too many elements from A on the left
            else:
                l = i + 1  # Too few elements from A on the left
