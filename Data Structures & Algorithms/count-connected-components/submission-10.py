class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        d= defaultdict(list)
        visit = set()

        for a, b in edges:
            d[a].append(b)
            d[b].append(a)

        def dfs(node, prev):

            if node in visit:

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