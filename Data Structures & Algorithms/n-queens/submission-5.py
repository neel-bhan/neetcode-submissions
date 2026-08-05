class Solution:

    def solveNQueens(self, n: int) -> List[List[str]]:  

        board = [[False for i in range(n)] for j in range(n)]   
        
        def valid(i, j):
            for n in board[i]:
                if n:
                    return False
            for n in board:
                if n[j]:
                    return False
            temp_i, temp_j = i, j
            while temp_i >= 0 and temp_j >= 0:
                if board[temp_i][temp_j]:
                    return False
                temp_i-=1
                temp_j-=1
            temp_i, temp_j = i, j
            while temp_i >= 0 and temp_j < len(board):
                if board[temp_i][temp_j]:
                    return False
                temp_i-=1
                temp_j+=1
            return True

            


        res = []

        def dfs(i):

            if i >= n:
                ans = []
                for b in board:
                    s = ""
                    for v in b:
                        if v:
                            s+="Q"
                        else:
                            s+="."
                    ans.append(s)
                res.append(ans)
                return
                    
            for j in range(n):
                if valid(i, j):
                    board[i][j] = True
                    dfs(i+1)
                    board[i][j] = False
        dfs(0)
        return res

        

