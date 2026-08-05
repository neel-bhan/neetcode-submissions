class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        d= defaultdict(list)
        for course, pre in prerequisites:
            d[pre].append(course)
        visited = set()
        res = set()
        res_li = []
        def dfs(c):
            if c in visited:
                return False
            if c in res:
                return True
            visited.add(c)
            
            for nei in d[c]:
                if not dfs(nei):
                    return False
            visited.remove(c)
            
            res_li.append(c)
            res.add(c)
            
            d[c] = []

            
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []


        return res_li[::-1]
