class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = defaultdict(list)
        for k, v in prerequisites:
           d[k].append(v)
        visited = [False for _ in range(numCourses)]
        print(visited)
        def dfs(course):
            if visited[course]:
                return False
            visited[course] = True
            for pre in d[course]:
                if not dfs(pre):
                    return False
            visited[course] = False
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


        