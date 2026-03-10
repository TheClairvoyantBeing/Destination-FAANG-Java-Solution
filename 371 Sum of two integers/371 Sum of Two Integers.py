# Leetcode Link: https://leetcode.com/problems/sum-of-two-integers/
# **************** Python Solution ***********************
# ---------- Question ----------
# Calculate sum of two integers without using + or - operators.
# ---------- Approach ----------
# Bit manipulation: XOR gives sum without carry, AND gives carry positions.
# Shift carry left and repeat. Use 32-bit mask for Python's infinite-precision ints.
# Time: O(1) — at most 32 iterations | Space: O(1)
class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        MAX = 0x7FFFFFFF
        while b != 0:
            carry = (a & b) & MASK
            a = (a ^ b) & MASK
            b = (carry << 1) & MASK
        return a if a <= MAX else ~(a ^ MASK)
