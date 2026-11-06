class Solution:
     def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        d = {}
        if len(points) == 1:
            return 0
        h = []
        n = len(points)
        def find(ele):
            if d[ele] == -1:
                return ele
            d[ele] = find(d[ele])
            return d[ele]

        for i in range(n):
            for j in range(i):
                cost = abs(points[i][1] - points[j][1]) + abs(points[i][0] - points[j][0])
                heapq.heappush(h, (cost, i, j))
        res = 0
        num = 0
        while h:
            cost, ele1, ele2 = heapq.heappop(h)
            if ele1 not in d:
                d[ele1] = -1
            if ele2 not in d:
                d[ele2] = -1
            p1, p2 = find(ele1), find(ele2)
            if p1 == p2:
                continue

            d[p1] = p2
            res += cost
            num += 1

            if num == n-1:
                return res


       