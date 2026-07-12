class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        ROWS = len(grid)
        COLS = len(grid[0])


        def bfs():
            q = deque()
            fresh = 0
            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == 2:
                        q.append((r,c))
                    if grid[r][c] == 1:
                        fresh += 1
            time = 0
            while q and fresh > 0:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    print(q)
                    for ar, ac in directions:
                        nr, nc = ar + r, ac + c 
                        
                        if ROWS > nr >= 0 and COLS > nc >= 0 and grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            q.append((nr, nc))
                            fresh-=1
                time += 1
            print(fresh)
            return time if fresh <= 0 else -1
        return bfs()

        