# Leetcode Link: https://leetcode.com/problems/reverse-bits/
# **************** Python Solution ***********************
# ---------- Question ----------
# Reverse bits of a given 32 bits unsigned integer.
# Example: 00000010100101000001111010011100 -> 00111001011110000010100101000000
# ---------- Approach ----------
# Extract each bit from LSB of n and place it at the mirrored position in result.
# Time: O(1) — always 32 iterations | Space: O(1)
class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            bit = (n >> i) & 1              # Extract i-th bit from right
            result |= bit << (31 - i)       # Place it at mirrored position
        return result
