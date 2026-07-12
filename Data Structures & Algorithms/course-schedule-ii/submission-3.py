class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        for k, v in prerequisites:
           d[k].append(v)
        visited = [False for _ in range(numCourses)]
        print(visited)
        output = []
        cycle = set()
        def dfs(course):
            if visited[course]:
                return False
            if course in cycle:
                return True
            visited[course] = True
            for pre in d[course]:
                if not dfs(pre):
                    return False
            visited[course] = False
            output.append(course)
            cycle.add(course)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return output