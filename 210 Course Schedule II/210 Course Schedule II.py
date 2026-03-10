# Leetcode Link: https://leetcode.com/problems/course-schedule-ii/
# **************** Python Solution ***********************
# ---------- Question ----------
# Return the ordering of courses you should take to finish all courses, or [] if impossible.
# Example: numCourses=4, prerequisites=[[1,0],[2,0],[3,1],[3,2]] -> [0,2,1,3] or [0,1,2,3]
# ---------- Approach ----------
# Topological sort using Kahn's algorithm (BFS with in-degree tracking).
# Time: O(V + E) | Space: O(V + E)
from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        for crs, pre in prerequisites:
            graph[pre].append(crs)
            in_degree[crs] += 1
        queue = deque(i for i in range(numCourses) if in_degree[i] == 0)
        order = []
        while queue:
            course = queue.popleft()
            order.append(course)
            for next_crs in graph[course]:
                in_degree[next_crs] -= 1
                if in_degree[next_crs] == 0:
                    queue.append(next_crs)
        return order if len(order) == numCourses else []
