# Leetcode Link: https://leetcode.com/problems/number-of-1-bits/
# **************** Python Solution ***********************
# ---------- Question ----------
# Return the number of '1' bits (Hamming weight) of an unsigned integer.
# Example: n=11 (binary: 1011) -> 3
# ---------- Approach ----------
# Check each bit using AND with 1, then right-shift.
# Time: O(1) — at most 32 bits | Space: O(1)
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1  # Add 1 if LSB is set
            n >>= 1         # Shift right to check next bit
        return count
