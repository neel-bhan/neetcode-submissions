class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        qu = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    qu.append((i,j))
        directions = [[1,0], [-1,0], [0,1], [0, -1]]
        res = -1

        while qu:
            res +=1 
            for i in range(len(qu)):
                cur = qu.popleft()
                for di, dj in directions:
                    new_i, new_j = cur[0] + di, cur[1] + dj
                    if new_i in range(len(grid)) and new_j in range(len(grid[0])) and grid[new_i][new_j] == 1:
                        qu.append((new_i, new_j))
                        grid[new_i][new_j] = 2

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1

           
        return max(res, 0)