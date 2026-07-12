class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
            
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        def dfs(node, par):

            if node in visited:
                return

            visited.add(node)
            for nei in adj[node]:
                if nei == par:
                    continue
                dfs(nei, node)

        time = 0
        for i in range(n):
            if i not in visited:
                dfs(i, -1)
                time += 1
        return time
