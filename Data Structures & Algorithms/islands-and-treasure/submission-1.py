class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        INF = 2147483647

        def bfs(r , c):
            count = 0
            q = deque([(r,c)])
            visited = [[False] * COLS for _ in range(ROWS)]
            visited[r][c] =  True   
            while q:
                for _ in range(len(q)):
                    l, r = q.popleft()
                    if grid[l][r] == 0:
                        return count
                
                    for dr, dc in directions:
                        nr, nc = l + dr, dc + r
                        if ROWS > nr >= 0 and COLS > nc >= 0 and not visited[nr][nc] and grid[nr][nc] != -1:
                            q.append((nr,nc))
                            visited[nr][nc] = True
                count += 1 
            return INF

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == INF:
                    grid[r][c] = bfs(r,c)

        