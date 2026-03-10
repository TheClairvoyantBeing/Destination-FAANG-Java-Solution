# Leetcode Link: https://leetcode.com/problems/course-schedule/
# **************** Python Solution ***********************
# ---------- Question ----------
# There are numCourses courses with prerequisite pairs. Return true if you can finish all courses.
# Example: numCourses=2, prerequisites=[[1,0]] -> True
# ---------- Approach ----------
# Topological sort via DFS cycle detection. If a cycle exists, courses can't be completed.
# Time: O(V + E) | Space: O(V + E)
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        graph = defaultdict(list)
        for crs, pre in prerequisites:
            graph[crs].append(pre)
        # 0=unvisited, 1=visiting (current path), 2=visited (safe)
        state = [0] * numCourses
        def dfs(course):
            if state[course] == 1: return False  # Cycle found
            if state[course] == 2: return True   # Already verified
            state[course] = 1
            for pre in graph[course]:
                if not dfs(pre): return False
            state[course] = 2
            return True
        return all(dfs(i) for i in range(numCourses))
