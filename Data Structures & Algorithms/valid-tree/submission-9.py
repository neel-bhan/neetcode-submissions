class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        d = defaultdict(list)
        for p,c in edges:
            if p == c:
                return False
            d[c].append(p)
            d[p].append(c)

        print(d)
        def dfs(cur, prev):
            if cur in visited:
                return False
            visited.add(cur)
            for nei in d[cur]:
                if nei == prev:
                    continue
                if not dfs(nei, cur):
                    return False
            return True
        
        

        if dfs(0, -1) and len(visited) == n:
            return True
        return False



        