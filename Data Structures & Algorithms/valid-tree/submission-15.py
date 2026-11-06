class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        d = defaultdict(list)

        for x, y in edges:
            d[x].append(y)
            d[y].append(x)

        seen = set()

        def dfs(i, prev):
            if i in seen:
                return False
            seen.add(i)

            for nei in d[i]:
                if nei == prev:
                    continue
                if not dfs(nei, i):
                    return False
            return True

        if not dfs(0, None):
            return False
        return len(seen) == n