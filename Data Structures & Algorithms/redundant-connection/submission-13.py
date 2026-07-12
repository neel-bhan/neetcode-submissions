class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        from collections import defaultdict
        from typing import List

        d = defaultdict(list)
        for a, b in edges:
            d[a].append(b)
            d[b].append(a)

        visit = set()
        cycleStart = -1

        def finds(node, prev):
            nonlocal cycleStart

            if node in visit:
                cycleStart = node
                return True

            visit.add(node)

            for nei in d[node]:
                if nei == prev:
                    continue

                if finds(nei, node):
                    return True

            return False

        finds(1, -1)

        path = []

        cycle = set()

        def dfs(node, prev):
            path.append(node)


            for nei in d[node]:
                if nei == prev:
                    continue

                if nei == cycleStart and len(path) >= 3:
                    cycle.update(path)
                    return True

                if nei not in path:
                    if dfs(nei, node):
                        return True

            path.pop()

            return False

        dfs(cycleStart, -1)

        for a, b in reversed(edges):
            if a in cycle and b in cycle:
                return [a, b]

        return []