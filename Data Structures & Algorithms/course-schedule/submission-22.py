class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for i, j in prerequisites:
            adj[i].append(j)
        path = set()
        seen = set()
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
            return True
        
        for i in range(numCourses):

            if not dfs(i):
                return False
        return len(seen) == numCourses
        