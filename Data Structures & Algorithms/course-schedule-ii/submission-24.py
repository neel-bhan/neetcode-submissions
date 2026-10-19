class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        d= defaultdict(list)
        for course, pre in prerequisites:
            d[pre].append(course)
        path = set()
        seen = set()
        res_li = []
        def dfs(c):
            if c in path:
                return False
            if c in seen:
                return True
            path.add(c)
            
            for nei in d[c]:
                if not dfs(nei):
                    return False
            path.remove(c)
            
            res_li.append(c)
            seen.add(c)
            
            d[c] = []

            return True
        for i in range(numCourses):
            if not dfs(i):
                return []


        return res_li[::-1]
