# Leetcode Link: https://leetcode.com/problems/reverse-integer/

# **************** Python Solution ***********************

# ---------- Question ----------
# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer
# range [-2^31, 2^31 - 1], then return 0.
#
# Example:
#   Input: x = 123   ->  Output: 321
#   Input: x = -123  ->  Output: -321
#   Input: x = 120   ->  Output: 21

# ---------- Approach ----------
# Convert to string, reverse, convert back. Handle sign separately.
# Check for 32-bit integer overflow before returning.
#
# Time Complexity : O(log x) — number of digits
# Space Complexity: O(log x) — for the string representation

class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
        x = abs(x)
        reversed_num = int(str(x)[::-1])  # Reverse the string of digits
        result = sign * reversed_num

        # Check 32-bit signed integer overflow
        if result < -2**31 or result > 2**31 - 1:
            return 0
        return result
