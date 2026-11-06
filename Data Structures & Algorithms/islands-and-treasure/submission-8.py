class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        q = deque()
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    q.append((i, j))
        level = 1
        dir = [[1,0], [0,1], [0, -1], [-1, 0]]
        while q:
            for i in range(len(q)):
                ele = q.popleft()
                for dx, dy in dir:
                    nx, ny = ele[0] + dx, ele[1] + dy
                    if nx in range(n) and ny in range(m) and grid[nx][ny] == 2147483647:
                        grid[nx][ny] = level
                        q.append((nx,ny))
            level += 1


        