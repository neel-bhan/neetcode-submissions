from collections import defaultdict
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for course, prereq in prerequisites:
            graph[course].append(prereq)

        visiting = [False] * numCourses

        def dfs(course):
            if visiting[course]:
                return False  # cycle detected

            if graph[course] == []:
                return True   # no prereqs or already checked

            visiting[course] = True

            for prereq in graph[course]:
                if not dfs(prereq):
                    return False

            visiting[course] = False
            graph[course] = []  # memoize as safe

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True