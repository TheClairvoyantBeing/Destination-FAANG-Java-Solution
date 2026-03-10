# Leetcode Link: https://leetcode.com/problems/high-five/
# **************** Python Solution ***********************
# ---------- Question ----------
# Given list of [id, score] pairs, compute the average of top 5 scores for each student.
# Return sorted by student id.
# ---------- Approach ----------
# Group scores by student id, sort descending, take top 5 average.
# Time: O(n log n) | Space: O(n)
from collections import defaultdict
class Solution:
    def highFive(self, items):
        scores = defaultdict(list)
        for student_id, score in items:
            scores[student_id].append(score)
        result = []
        for student_id in sorted(scores):
            top5 = sorted(scores[student_id], reverse=True)[:5]
            avg = sum(top5) // len(top5)
            result.append([student_id, avg])
        return result
