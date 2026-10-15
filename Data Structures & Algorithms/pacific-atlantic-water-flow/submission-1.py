class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        p = set()
        a = set()

        dir = [[0,1], [1,0], [0, -1], [-1, 0]]
        arr = set()
        def dfs(i, j, w):
            arr = p if w == "p" else a
            arr.add((i,j))
            for x, y in dir:
                ni, nj = i + x, j + y
                if (ni,nj) not in arr and ni in range(len(grid)) and nj in range(len(grid[0])):
                    if grid[ni][nj] >= grid[i][j]:
                        dfs(ni, nj, w)

        for i in range(len(grid)):
            dfs(i, 0, 'p')
            dfs(i, len(grid[0]) -1, 'a')
        for i in range(len(grid[0])):
            dfs(0, i ,"p")
            dfs(len(grid) -1 , i, 'a')
        print(a, p)
        res = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) in a and (i, j) in p:
                    res.append([i,j])
        return res

        
        