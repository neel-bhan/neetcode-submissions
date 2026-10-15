class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indegree = defaultdict(int)
        for i, j in prerequisites:
            adj[i].append(j)

        path = set()
        seen = set()
        res = []
        def dfs(i):
            if i in path:
                return False
            if i in seen:
                return True
            seen.add(i)
            path.add(i)
            for nei in adj[i]:
                if not dfs(nei):
                    return False
            path.remove(i)
            adj[i] = []
            res.append(i)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res