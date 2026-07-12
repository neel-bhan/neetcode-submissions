class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(i, j, index):
            
            nonlocal res
            
            if(board[i][j] != word[index] or (i, j)in seen):
                return
            print(board[i][j])
            if index >= len(word)-1:
                res = True
                return
            
            seen.add((i,j))
            if(i > 0):
                dfs(i-1, j, index + 1)
            if(j > 0):
                dfs(i, j-1, index + 1)
            if(i < len(board) -1):
                dfs(i+1, j, index + 1)
            if(j < len(board[0]) -1):
                dfs(i, j+1, index + 1)
           
            seen.remove((i, j))
            


        res = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                seen = set()
                if(board[i][j] == word[0]):
                    dfs(i, j, 0)
        return res