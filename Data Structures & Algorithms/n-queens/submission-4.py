class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        subset = [["."] * n for _ in range(n)]

        cols = set()
        diag1 = set()
        diag2 = set()

        def dfs(r):
            if r == n:
                res.append(["".join(row) for row in subset])
                return

            for c in range(n):
                if c in cols or (r - c) in diag1 or (r + c) in diag2:
                    continue

                subset[r][c] = "Q"
                cols.add(c)
                diag1.add(r - c)
                diag2.add(r + c)

                dfs(r + 1)

                subset[r][c] = "."
                cols.remove(c)
                diag1.remove(r - c)
                diag2.remove(r + c)

        dfs(0)
        return res