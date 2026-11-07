class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        h = [] 

        seen = set()
        
        d = defaultdict(list)
        for s, de, c in flights:
            d[s].append((de, c))
        heapq.heappush(h, (0,0, src)) #cost, k , cur

        while h:
            cost, num, cur = heapq.heappop(h)
            if cur == dst:
                return cost
            if num == k +1:
                continue
            if (cur, num)  in seen:
                continue
            seen.add((cur, num))
            for newd, newc in d[cur]:
                heapq.heappush(h, (cost + newc, num + 1, newd))
        return -1
            

