class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        res = float("inf")
        memo = {}
        def dfs(l, r, num):
            nonlocal res
            if r == len(word2):
                return len(word1) - l
            if l == len(word1):
                return len(word2) - r
                return res
            if (l, r) in memo:
                return memo[(l, r)]
            if word1[l] == word2[r]:
                memo[(l, r)] = dfs(l + 1, r + 1, num)
            else:
                memo[(l, r)] = 1 + min(dfs(l+1, r, num + 1), dfs(l, r + 1, num +1), dfs(l + 1, r + 1, num + 1))
            return memo[(l,r)]
        return dfs(0,0,0)

            
            
        