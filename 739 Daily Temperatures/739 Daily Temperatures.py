# Leetcode Link: https://leetcode.com/problems/daily-temperatures/
# **************** Python Solution ***********************
# ---------- Question ----------
# Given array of daily temperatures, for each day find how many days until a warmer temperature.
# Example: temperatures=[73,74,75,71,69,72,76,73] -> [1,1,4,2,1,1,0,0]
# ---------- Approach ----------
# Monotonic decreasing stack: store indices. When a warmer day arrives, pop and compute difference.
# Time: O(n) | Space: O(n)
class Solution:
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        result = [0] * n
        stack = []
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                result[idx] = i - idx  # Days until warmer
            stack.append(i)
        return result
