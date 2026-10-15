class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        seen = set()
        adj = defaultdict(list)
        
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
        
        def dfs(i):
            if i in seen:
                return False
            seen.add(i)
            for nei in adj[i]:
                dfs(nei)
            return True
        res = 0
        for i in range(n):
            if dfs(i):
                res += 1
        return res