# Leetcode Link: https://leetcode.com/problems/multiply-strings/

# **************** Python Solution ***********************

# ---------- Question ----------
# Given two non-negative integers num1 and num2 represented as strings,
# return the product of num1 and num2, also as a string.
# You must not convert the inputs to integers directly.
#
# Example:
#   Input: num1 = "123", num2 = "456"  ->  Output: "56088"

# ---------- Approach ----------
# Grade-school multiplication — multiply digit by digit, accumulating results
# in a result array at the correct positions.
# result[i+j] and result[i+j+1] store the partial product of digits at i and j.
#
# Time Complexity : O(m * n) — where m, n are the lengths of the two strings
# Space Complexity: O(m + n) — for the result array

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        result = [0] * (len(num1) + len(num2))

        # Multiply digit by digit from right to left
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                p1, p2 = i + j, i + j + 1  # Two positions this product affects
                total = mul + result[p2]    # Add existing value at lower position
                result[p2] = total % 10     # Keep ones digit
                result[p1] += total // 10   # Carry to higher position

        result_str = ''.join(map(str, result))
        return result_str.lstrip('0') or '0'  # Remove leading zeros
