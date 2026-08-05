class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d= defaultdict(list)
        for course, pre in prerequisites:
            d[pre].append(course)
        visited = set()
        res = set()
        def dfs(c):
            if c in visited:
                return False
            visited.add(c)
            res.add(c)
            for nei in d[c]:
                if not dfs(nei):
                    return False
            visited.remove(c)
            d[c] = []
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        if len(res) != numCourses:
            return False

        return True

        