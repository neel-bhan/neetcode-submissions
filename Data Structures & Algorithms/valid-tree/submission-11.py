class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        d= defaultdict(list)
        visit = set()
        cycle = set()
        for a, b in edges:
            d[a].append(b)
            d[b].append(a)
        cycle = False
        def dfs(node, prev):
            nonlocal cycle
            if node in visit:
                cycle = True
                return
            visit.add(node)
            for nei in d[node]:
                if nei == prev:
                    continue
                dfs(nei, node)

        dfs(0, -1)
        return len(visit) == n and not cycle               