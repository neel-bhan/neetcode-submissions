class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        h = []

        heapq.heappush(h, (0, src, 0))

        d = defaultdict(list)
        seen = {}
        for s, de, c in flights:
            d[s].append((de, c))

        while h:
            cost, source, num = heapq.heappop(h)

            if source in seen and seen[source] < num:
                continue
            
            seen[source] = num
            if source == dst:
                return cost
            if k+1 == num:
                continue

            for  dest, cur_cost in d[source]:
                if num == k+1:
                    continue
                
                heapq.heappush(h, (cost + cur_cost, dest, num +1))
                
                


        return -1


