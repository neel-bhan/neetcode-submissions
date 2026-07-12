class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        fail = True
        memo = {}
        def dfs(amount):
            nonlocal fail
            if amount == 0:
                fail = False
                return 0
            if amount <= 0:
                return float("inf")
            if amount in memo:
                return memo[amount]
            mini = float("inf")
            for i in coins:
                mini = min(mini, dfs(amount - i))
            memo[amount] = 1 + mini
            return 1 + mini
        ans = dfs(amount)
        return -1 if fail else ans




        