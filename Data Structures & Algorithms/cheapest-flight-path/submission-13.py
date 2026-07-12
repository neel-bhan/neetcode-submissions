class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #d[start] = {(stop, cost)}
        d = defaultdict(list)
        #(cost, stop, len)
        qu = []

        for f in flights:
            sr, ds, cost = f
            d[sr].append((ds, cost))
        
        for f in d[src]:
            heapq.heappush(qu, (f[1], f[0], 0))
        print(d)
        print()
        print(qu)

        while qu:
            cost, start, l = heapq.heappop(qu)
            if start == dst:
                return cost
            if k <= l:
                continue
            for stop, add in d[start]:
                heapq.heappush(qu, (cost + add, stop, l + 1))

        return -1
        

        