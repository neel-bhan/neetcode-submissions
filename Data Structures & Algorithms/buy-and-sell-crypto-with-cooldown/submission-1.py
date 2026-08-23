class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dfs(i, b):
            if i >= len(prices):
                return 0
            if (i, b) in memo:
                return memo[(i,b)]
            if b:
                memo[(i,b)] = max(prices[i] + dfs(i+2, False), dfs(i+1, True))
            else:
                memo[(i,b)] = max(-prices[i] + dfs(i+1, True), dfs(i+1, False))
            return memo[(i,b)]
        print(memo)
        res=  dfs(0, False)
        print(memo)
        return res