class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        wd = set(wordDict)

        memo = {}

        def dfs(i):
            if i >= len(s):
                return True
            if i in memo:
                return memo[i]
            for j in range(i, len(s)+1):

                if s[i:j]in wd:
                    if dfs(j):
                        return True
            memo[i] = False
            return False
        return dfs(0)
            