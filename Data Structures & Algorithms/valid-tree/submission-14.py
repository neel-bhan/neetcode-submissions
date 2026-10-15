class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        path = set()
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
                    if not dfs(nei, i):
                        return False

            return True
        if not dfs(0,-1):
            return False
        return len(seen) == n
                

        