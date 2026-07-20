class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r,l,b,t=len(matrix[0]), 0, 0, len(matrix)
        i, j = 0,0
        res = []
        while l < r and b < t:
            for i in range(l, r):
                res.append(matrix[b][i])
            b+=1
            
            for i in range(b, t):
                res.append(matrix[i][r-1])    
            r-=1
            print(res)
            if l >= r or b >= t:
                break
            for i in range(r-1, l-1, -1):

                res.append(matrix[t-1][i])
            t-=1
            
            for i in range(t-1, b-1, -1):
                res.append(matrix[i][l])
            l+=1
        return res
            


