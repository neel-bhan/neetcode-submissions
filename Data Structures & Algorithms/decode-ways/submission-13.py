class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {len(s): 1}

        def dfs(i):
            if i in memo:
                return memo[i]
            if s[i] == '0':
                return 0
            res = dfs(i+1)
            if i < len(s) - 1 and (int(s[i]) == 1 or (int(s[i]) == 2 and (0<=int(s[i+1]) <= 6))):
                res += dfs(i+2)
            memo[i] = res
            return memo[i]
        return dfs(0)
            
