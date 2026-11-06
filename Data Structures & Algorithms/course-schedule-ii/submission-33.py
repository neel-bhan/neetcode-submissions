class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        d= defaultdict(list)
        for course, pre in prerequisites:
            d[course].append(pre)

        seen = set()
        path = set()
        res = []

        def dfs(course):
            if course in path:
                return False
            if course in seen:
                return True
            path.add(course)
            seen.add(course)
            for pre in d[course]:
                if not dfs(pre):
                    return False
            path.remove(course)
            res.append(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return res
