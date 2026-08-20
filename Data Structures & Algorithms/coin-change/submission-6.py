class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = {}
        coins.sort(reverse=True)

        def dfs(i, a):
            if (i, a) in memo:
                return memo[(i,a)]
            if a == amount:
                return 0
            if i >= len(coins) or a > amount:
                return float("inf")
            take = 1 + dfs(i, a + coins[i])
            skip = dfs(i+1, a)
            res = min(take, skip)
            memo[(i,a)] = res
            return res

        ans = dfs(0, 0)
        return -1 if ans == float('inf') else ans

        