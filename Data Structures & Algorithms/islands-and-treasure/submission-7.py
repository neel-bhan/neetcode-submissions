class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        dir = [[0,1], [1,0], [0, -1], [-1, 0]]
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i,j))
        cur = 0
        while q:
            cur += 1
            for i in range(len(q)):
                i,j = q.popleft()
                for di, dr in dir:
                    if i + di in range(len(grid)) and j + dr in range(len(grid[0])) and grid[i+di][j+dr] == 2147483647:
                        grid[i+di][j+dr] = cur
                        q.append((i+di, j + dr))

                    

