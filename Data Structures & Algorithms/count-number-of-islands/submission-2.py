class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dir = [[0,1], [1,0], [0, -1], [-1, 0]]

        def dfs(i, j):
            if i not in range(len(grid)) or j not in range(len(grid[0])) or grid[i][j] == "0":
                return False
            grid[i][j] = "0"
            for di, dj in dir:
                dfs(i + di, j + dj)
            return True
        
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if dfs(i , j):
                    res += 1
        return res
