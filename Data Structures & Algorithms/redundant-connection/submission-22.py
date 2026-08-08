class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        d = defaultdict(list)
        for a, b in edges:
            d[a].append(b)
            d[b].append(a)

        seen = set()
        cycleStart = -1

        def dfs(node, prev):
            nonlocal cycleStart
            if node in seen:
                cycleStart = node
                return True
            seen.add(node)
            for nei in d[node]:
                if nei == prev:
                    continue
                if dfs(nei, node):
                    return True
            return False
        dfs(edges[0][0], -1)
        cycle_s = set()
        def cycle(node, prev, target):
            nonlocal cycleStart
            if node == target and prev != -1:
                return True
            cycle_s.add(node)
            for nei in d[node]:
                if nei == prev:
                    continue
                if cycle(nei, node, target):
                    return True
            cycle_s.remove(node)
            return False

        cycle(cycleStart, -1, cycleStart)
        print(cycle_s)
        for a, b in edges[::-1]:
            if a in cycle_s and b in cycle_s:
                return [a, b]

        




