# Leetcode Link: https://leetcode.com/problems/powx-n/

# **************** Python Solution ***********************

# ---------- Question ----------
# Implement pow(x, n) which calculates x raised to the power n.
#
# Example:
#   Input: x = 2.0, n = 10  ->  Output: 1024.0
#   Input: x = 2.0, n = -2  ->  Output: 0.25

# ---------- Approach ----------
# Fast Exponentiation (Binary Exponentiation):
#   - If n is even: x^n = (x^2)^(n/2)
#   - If n is odd:  x^n = x * x^(n-1)
# Handle negative exponents by taking 1/x and negating n.
#
# Time Complexity : O(log n)
# Space Complexity: O(1) — iterative approach

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x  # Invert base for negative exponent
            n = -n

        result = 1
        while n > 0:
            if n % 2 == 1:      # If current exponent is odd, multiply result by x
                result *= x
            x *= x              # Square the base
            n //= 2             # Halve the exponent

        return result
