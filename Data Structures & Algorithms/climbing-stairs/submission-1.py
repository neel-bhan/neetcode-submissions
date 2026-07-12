class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def dfs(i):
            
            if i <= 0:
                return i == 0
            if i in cache:
                return cache[i]
            else:
                cache[i] = dfs(i - 1) + dfs(i - 2)
                return dfs(i - 1) + dfs(i - 2)

        return dfs(n)