class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def findrc(num):
            return (num//len(matrix[0]), num % len(matrix[0]))

        l= 0
        r = len(matrix) * len(matrix[0]) - 1
        while l <= r:
            m = (l+r)//2
            row, col = findrc(m)
            if matrix[row][col] > target:
                r = m-1
            elif matrix[row][col] < target:
                l = m+1
            else:
                return True
        return False

       