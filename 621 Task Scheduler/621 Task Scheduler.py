# Leetcode Link: https://leetcode.com/problems/task-scheduler/
# **************** Python Solution ***********************
# ---------- Question ----------
# Given tasks and cooldown period n, return the least intervals the CPU needs to finish all tasks.
# Example: tasks=["A","A","A","B","B","B"], n=2 -> 8 (A B idle A B idle A B)
# ---------- Approach ----------
# Greedy math: the most frequent task dictates the schedule. Answer = max(len(tasks), formula).
# Formula: (max_freq - 1) * (n + 1) + count_of_tasks_with_max_freq
# Time: O(n) | Space: O(1) — at most 26 task types
from collections import Counter
class Solution:
    def leastInterval(self, tasks, n: int) -> int:
        count = Counter(tasks)
        max_freq = max(count.values())
        max_count = sum(1 for v in count.values() if v == max_freq)
        result = (max_freq - 1) * (n + 1) + max_count
        return max(result, len(tasks))
