class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        d= defaultdict(list)
        visit = set()

        for a, b in edges:
            d[a].append(b)
            d[b].append(a)

        res = 0
        seen = set()
        def dfs(i, prev):
            if i in seen:
                return False
            seen.add(i)

            for nei in d[i]:
                if nei == prev:
                    continue
                dfs(nei, i)
            return True

        for i in range(n):
            if dfs(i, None):
                res += 1
        return res
