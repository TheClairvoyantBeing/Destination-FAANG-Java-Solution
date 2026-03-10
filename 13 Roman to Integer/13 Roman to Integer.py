# Leetcode Link: https://leetcode.com/problems/roman-to-integer/

# **************** Python Solution ***********************

# ---------- Question ----------
# Roman numerals are represented by seven symbols: I, V, X, L, C, D, M.
# Given a roman numeral, convert it to an integer.
# Subtraction rule: I before V/X means subtract, X before L/C means subtract, etc.
#
# Example:
#   Input: s = "MCMXCIV"  ->  Output: 1994
#   Explanation: M=1000, CM=900, XC=90, IV=4

# ---------- Approach ----------
# Scan left to right. If the current value is less than the next value,
# subtract it (subtraction rule); otherwise, add it.
#
# Time Complexity : O(n) — single pass
# Space Complexity: O(1) — fixed-size lookup table

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0

        for i in range(len(s)):
            # If current value < next value, subtract (e.g., IV = 4)
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                result -= roman[s[i]]
            else:
                result += roman[s[i]]

        return result
