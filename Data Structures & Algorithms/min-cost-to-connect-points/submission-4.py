class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        d = {i: -1 for i in range(n)}
        edges = []
        

        def find(num):
            while -1 != d[num]:
                num = d[num]
            return num


        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                distance = abs(x1 - x2) + abs(y1 - y2)
                heapq.heappush(edges, (distance, i, j))
        res = 0
        num = 0
        while edges:
            di, i , j = heapq.heappop(edges)
            if num == n:
                return
            r_i, r_j = find(i), find(j)
            if r_i == r_j:
                continue
            


            if d[i] == -1 and d[j] == -1:
                d[j] = i
            elif not r_i == r_j:
                d[r_j] = r_i 

            res += di
            num+= 1

            if num == n:
                break

            
        return res
            
        


