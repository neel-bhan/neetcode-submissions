class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
            
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        nodes = set(range(n))
        print(nodes)
        visited = set()
        def dfs(node, par):

            if node in visited:
                return
            if node in nodes:
                nodes.remove(node)
            visited.add(node)
            for nei in adj[node]:
                if nei == par:
                    continue
                dfs(nei, node)

        time = 0
        while nodes:
            dfs(nodes.pop(), -1)
            time += 1 
        return time
