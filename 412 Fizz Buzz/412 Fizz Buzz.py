# Leetcode Link: https://leetcode.com/problems/fizz-buzz/
# **************** Python Solution ***********************
# ---------- Question ----------
# For 1 to n: if divisible by 3 print "Fizz", by 5 print "Buzz", by both print "FizzBuzz",
# else print the number.
# ---------- Approach ----------
# Simple iteration with modulo checks. Order matters: check 15 (both) first.
# Time: O(n) | Space: O(n)
class Solution:
    def fizzBuzz(self, n: int):
        result = []
        for i in range(1, n + 1):
            if i % 15 == 0:   result.append("FizzBuzz")
            elif i % 3 == 0:  result.append("Fizz")
            elif i % 5 == 0:  result.append("Buzz")
            else:             result.append(str(i))
        return result
