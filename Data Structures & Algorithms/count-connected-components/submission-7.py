class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
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
        res = 0 
        for i in range(n):
            if not i in visit:

                dfs(i, -1)
                res+=1
        return res