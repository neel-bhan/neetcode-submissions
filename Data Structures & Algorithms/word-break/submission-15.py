class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        s_set = set(wordDict)
        memo = {}

        def dfs(i):
            if i == len(s):
                return True
            if i in memo:
                return memo[i]

            for new in range(i, len(s)+1):
                if s[i:new+1] in s_set:
                    if dfs(new+1):
                        memo[i] = True
                        return True
            memo[i] = False
            return False


        return dfs(0)
            






















        