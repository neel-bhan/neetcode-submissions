class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = {i: [] for i in range(numCourses)}
        for crs, pres in prerequisites:
            pre[crs].append(pres)

        visited = [False] * numCourses

        def dfs(course):
            if visited[course]:
                return False
            if pre[course] == []:
                return True

            visited[course] = True
            for p in pre[course]:
                if not dfs(p):
                    return False

            visited[course]= False
            pre[course] = []
            
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True

        

