class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        h = []
        maxval = 0 
        di = [[1,0],[0,1], [-1,0],[0,-1]]
        n = len(grid)
        heapq.heappush(h, (grid[0][0], 0, 0 ))
        seen = set()
        while h:

            val, x, y = heapq.heappop(h)
            maxval = max(maxval, val)

            if x == n-1 and y == n -1:
                return maxval
            
            for dx, dy in di:
                nx, ny = x + dx, y + dy
                if nx in range(n) and ny in range(n) and not (nx, ny) in seen:
                    seen.add((nx, ny))
                    heapq.heappush(h, (grid[nx][ny], nx, ny))

