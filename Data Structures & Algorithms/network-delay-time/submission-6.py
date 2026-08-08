class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        time = 0
        adj = defaultdict(list)
        qu = []
        
        for t in times:
            adj[t[0]].append((t[2], t[1]))

        seen = set()
        heapq.heappush(qu, (0, k))
        res = 0
        while qu and len(seen) < n:
            val, cur = heapq.heappop(qu)
            
            if cur in seen:
                continue
            seen.add(cur)
            res = max(res, val)
            for cost, nei in adj[cur]:
                if not nei in seen:
                    heapq.heappush(qu, (val + cost, nei))
                    
        return res if len(seen) >= n else -1

