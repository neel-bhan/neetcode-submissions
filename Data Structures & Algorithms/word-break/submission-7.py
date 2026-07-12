class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #d = {char: c}
        ws = set(wordDict)
        memo = [None for i in range(len(s))]
        print(memo)
        def dfs(index):

            if index == len(s):
                return True
            if memo[index] is not None:
                return memo[index]
            cur = ""
            for i in range(index, len(s)):
                cur += s[i]
                if cur in ws:
                    if dfs(i+1):
                        memo[index] = True
                        return True
            memo[index] = False
            return False
        return dfs(0)

        