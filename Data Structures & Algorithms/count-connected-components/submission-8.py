class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        seen = set()
        adj = defaultdict(list)
        
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
        
        def dfs(i, prev):
            if i in seen:
                return False
            seen.add(i)
            for nei in adj[i]:
                if nei != prev:
                    dfs(nei, i)
            return True
        res = 0
        for i in range(n):
            if dfs(i, -1):
                res += 1
        return res