class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre = {i: [] for i in range(numCourses)}
        for crs, pres in prerequisites:
            pre[crs].append(pres)

        visited = [False] * numCourses
        li = []
        def dfs(course):
            if visited[course]:
                return []

            visited[course] = True
            for p in pre[course]:
                if not dfs(p):
                    return []

            visited[course]= False
            print(course)
            if not course in res:
                res.add(course)
                li.append(course)
            
            pre[course] = []
            
            return True
        res = set()
        for c in range(numCourses):
            if not dfs(c):
                return []

        return li

        

