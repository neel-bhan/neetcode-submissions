class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        subset = [["." for _ in range(n)] for _ in range(n)]
        queens = []
        def dfs(i):
            nonlocal n
            r = i % n
            c = i // n
            
            if c >= n:
                if len(queens) >=n:
                    li = []
                    for ele in subset:
                        li.append(''.join(ele))
                    res.append(li)
                return

            if len(queens) >= n:
                li = []
                for ele in subset:
                    print(subset)
                    li.append(''.join(ele))
                res.append(li)
                return
            test = True
            for ele in queens:
                qr, qc = ele
                if qr == r or qc == c or (abs(qr - r) == abs(qc - c)):
                    test = False
            if test: 
                subset[r][c] = 'Q'
                queens.append((r,c))
                dfs(i+1)
                subset[r][c] = '.'
                queens.pop()
            dfs(i+1)
        dfs(0)
        return res


            

        