class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        directions = [
            (-1, 0),  
            (1, 0),   
            (0, -1),  
            (0, 1)    
        ] 
        memo = {}
        def dfs(i, j):
            res = 0
            if (i, j) in memo:
                return memo[(i,j)]
            for dr, dc in directions:
                if i + dr in range(len(matrix)) and j + dc in range(len(matrix[0])):
                    if matrix[i][j] < matrix[i + dr][j + dc]:
                        res = max(res, 1 + dfs(i +dr, j + dc))
            memo[(i,j)] = res
            return res
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res = max(res, 1 + dfs(i, j))
        return res 
