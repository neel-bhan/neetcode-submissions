class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        row, col = len(grid), len(grid[0])

        def dfs(r, c):
            for d in directions:
                x,y = d[0] + r, d[1] + c
                if(x >= 0 and y >= 0 and x < row and y < col and grid[x][y] != "0"):
                    grid[x][y] = "0"
                    dfs(x,y)
        res = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    dfs(i,j)
                    res +=1
        return res                