class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def dfs(a, i):
            if i >= len(coins):
                return 0
            if a == 0:
                return 1
            if (a, i) in memo:
                return memo[(a, i)]
            res = 0
            c = coins[i]
            if a - c >= 0:
                res = dfs(a-c, i)
            res += dfs(a, i+1)
            memo[(a,i )] = res
            return res
        return dfs(amount, 0)
