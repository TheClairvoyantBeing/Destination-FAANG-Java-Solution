# Leetcode Link: https://leetcode.com/problems/plus-one/

# **************** Python Solution ***********************

# ---------- Question ----------
# Given a non-empty array of decimal digits representing a non-negative integer,
# increment one to the integer. Digits are stored most significant digit first.
#
# Example:
#   Input: digits = [1,2,3]  ->  Output: [1,2,4]
#   Input: digits = [9,9,9]  ->  Output: [1,0,0,0]

# ---------- Approach ----------
# Traverse from the rightmost digit. If a digit is less than 9, increment it and return.
# If it's 9, set it to 0 (carry propagates). If all digits were 9, prepend a 1.
#
# Time Complexity : O(n) — worst case traverse all digits
# Space Complexity: O(1) — in-place (except the edge case of all 9s)

class Solution:
    def plusOne(self, digits):
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits     # No carry, done
            digits[i] = 0         # Carry: set to 0 and continue

        return [1] + digits       # All digits were 9 (e.g., 999 -> 1000)
