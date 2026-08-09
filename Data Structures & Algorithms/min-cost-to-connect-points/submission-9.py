class Solution:
     def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        d = {i:-1 for i in range(n)}

        def find(n):
            while d[n] != -1:
                n = d[n]
            return n

        h = []
        for i in range(n):
            for j in range(i):
                x_dif = abs(points[i][0] - points[j][0])
                y_dif = abs(points[i][1] - points[j][1])
                heapq.heappush(h, ((x_dif + y_dif), i, j))
        res = 0
        num = 0
        while h:
            di, i ,j  = heapq.heappop(h)
            r_i, r_j = find(i), find(j)

            if r_i == r_j:
                continue
            d[r_i] = r_j
            res += di
            num += 1

            if num == n:
                break
        return res

