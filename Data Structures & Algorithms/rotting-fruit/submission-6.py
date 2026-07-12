class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        ROWS = len(grid)
        COLS = len(grid[0])

        def bfs():

            fresh = 0
            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == 1:
                        fresh += 1

            time = 0 
            print(123)
            while fresh >= 0:
                flag = False
                for r in range(ROWS):
                    for c in range(COLS):
                        if grid[r][c] == 2:
                            for ar, ac in directions:
                                nr, nc = ar + r, ac + c
                                if nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] == 1:
                                    grid[nr][nc] = 3
                                    fresh -= 1
                                    flag = True
                if not flag:
                    break
                for r in range(ROWS):
                    for c in range(COLS):
                        if grid[r][c] == 3:
                            grid[r][c] = 2
                time += 1
            
            return time if fresh == 0 else -1


        return bfs()

        