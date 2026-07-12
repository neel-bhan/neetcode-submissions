class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROW, COL = len(board), len(board[0])

        def dfs(r, c):
            if r not in range(ROW) or c not in range(COL):
                print(r,c)
                return True
            if board[r][c] == "X" or visited[r][c]:
                return False
            visited[r][c] = True
            return dfs(r+1,c) or dfs(r-1,c) or dfs(r,c+1) or dfs(r,c-1)




        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == "O":
                    visited = [[False] * COL for _ in range(ROW)]
                    if not dfs(r, c):
                        board[r][c] =  "X"



        