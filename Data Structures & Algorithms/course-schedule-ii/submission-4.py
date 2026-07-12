class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        indegree = [0] * numCourses
        for k, v in prerequisites:
           d[v].append(k)
           indegree[k] += 1
        
        output = []
        def dfs(course):
            output.append(course)
            indegree[course] -=1
            for nxt in d[course]:
                indegree[nxt] -=1
                if indegree[nxt] == 0:
                    dfs(nxt)

        for i in range(numCourses):
            if indegree[i] == 0:
                dfs(i)
        print(output)
        return output if len(output) == numCourses else []
            









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