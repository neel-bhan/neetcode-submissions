class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = [0] * (n+1)
        cost.insert(0, 0)
        def dfs(i):
            if i >= len(cost):
                return 0

            if memo[i]:
                return memo[i]


            memo[i] = cost[i] + min(dfs(i+1), dfs(i+2))
            return memo[i]
        return dfs(0)

        