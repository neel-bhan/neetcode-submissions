class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        for i in range(len(matrix)//2):
            matrix[len(matrix)-i-1], matrix[i] = matrix[i], matrix[len(matrix)-i-1]

        for i in range(len(matrix)):
            for j in range(i+1, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i],    matrix[i][j]