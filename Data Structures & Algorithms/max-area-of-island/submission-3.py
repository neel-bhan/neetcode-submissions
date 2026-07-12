class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        row, col = len(grid), len(grid[0])

        def dfs(r, c):
            sum = 1
            grid[r][c] = 0
            for d in directions:
                x,y = d[0] + r, d[1] + c
                if(x >= 0 and y >= 0 and x < row and y < col and grid[x][y] != 0):
                    grid[x][y] = 0
                    sum += dfs(x,y)
                
            return sum

        res = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    res = max(dfs(i,j), res)
        return res    