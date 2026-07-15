class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}
        def dfs(l, r):
            if (l, r) in memo:
                return memo[(l,r)]
            if r == len(t):
                return 1
            if l == len(s):
                return 0
            res = 0
            if s[l] == t[r]:
                res += dfs(l + 1, r + 1)
            res += dfs(l+1, r)
            memo[(l,r)] = res
            return res 

        return dfs(0,0)