class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        max_val = 0
        n = len(grid)
        qu = []
        heapq.heappush(qu, (grid[0][0], 0, 0))
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()

        def bfs():
            while qu:

                nonlocal max_val
                level, i, j = heapq.heappop(qu)
                max_val = max(level, max_val)
                visited.add((i,j))

                if i == n-1 and j == n-1:
                    return max_val

                for dr, dc in directions:
                    n_r, n_c = i + dr, j + dc

                    if not (n_r in range(n) and n_c in range(n)) or (n_r,n_c) in visited:
                        continue

                    heapq.heappush(qu, (grid[n_r][n_c], n_r, n_c))

        return bfs()