class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        time = 0
        adj = defaultdict(list)
        qu = []


        for t in times:
            adj[t[0]].append((t[1], t[2]))
        visited = set()
        visited.add(k)
        for i in adj[k]:
            heapq.heappush(qu, (i[1], k, i[0]))
        time = {k : 0}
        res = 0
        while qu and len(visited) < n:
            edge = heapq.heappop(qu)
            cur = edge[2]
            if cur in visited:
                continue
            time[cur] = edge[0]
            res = max(res, time[cur])
            visited.add(cur)
            for i in adj[cur]:
                heapq.heappush(qu, (time[cur]+i[1], cur, i[0]))
        print(visited)
        if len(visited) != n:
            return -1
        return res
            
            


        