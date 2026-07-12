class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        INF = 2147483647

        def bfs():
            count = 1
            
            
            q = deque([])
            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == 0:
                        q.append((r,c))

                        
                    
  
            while q:
                for _ in range(len(q)):
                    l, r = q.popleft()
                    for dr, dc in directions:
                        nr, nc = l + dr, dc + r
                        if ROWS > nr >= 0 and COLS > nc >= 0 and grid[nr][nc] == INF:
                            
                            q.append((nr,nc))

                            grid[nr][nc] = count
                count += 1 
            return
        bfs()

        

        

        