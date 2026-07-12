class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights),len(heights[0])
        pc, at = set(), set()


        
        def dfs(r, c, arr, ph):
            if ((r,c) in arr or r not in range(ROWS) or c not in range(COLS) or heights[r][c] < ph):
                return

            arr.add((r,c))

            dfs(r+1, c, arr, heights[r][c])
            dfs(r-1, c, arr, heights[r][c])
            dfs(r, c+1, arr, heights[r][c])
            dfs(r, c-1, arr, heights[r][c])

        for i in range(ROWS):
            dfs(i, 0, pc, 0)
            dfs(i, COLS-1, at, 0)
        for i in range(COLS):
            dfs(0, i, pc, 0)
            dfs(ROWS-1, i, at, 0)
        res = []
        print(at)
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pc and (r,c) in at:
                    res.append((r,c))
        return res




