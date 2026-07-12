class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        d = defaultdict(list)
        
        for p, c in edges:
            d[p].append(c)
            d[c].append(p)
        visited = set()
        def dfs(cur, prev):
            if cur in visited:
                return
            visited.add(cur)

            for nei in d[cur]:
                if nei == prev:
                    continue 
                dfs(nei, cur)

        res = 0
        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i, -1)
        return res