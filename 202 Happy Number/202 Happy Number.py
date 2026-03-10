# Leetcode Link: https://leetcode.com/problems/happy-number/
# **************** Python Solution ***********************
# ---------- Question ----------
# A happy number: replace with sum of squares of its digits repeatedly.
# If it reaches 1, it's happy. If it loops endlessly, it's not.
# Example: 19 -> 82 -> 68 -> 100 -> 1 (happy!)
# ---------- Approach ----------
# Floyd's cycle detection (slow/fast) or use a set to detect loops.
# Time: O(log n) | Space: O(1) with Floyd's
class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_squares(num):
            total = 0
            while num > 0:
                digit = num % 10
                total += digit * digit
                num //= 10
            return total
        slow = n
        fast = sum_squares(n)
        while fast != 1 and slow != fast:
            slow = sum_squares(slow)
            fast = sum_squares(sum_squares(fast))
        return fast == 1
