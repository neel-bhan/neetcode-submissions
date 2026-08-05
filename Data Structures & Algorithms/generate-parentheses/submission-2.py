class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        open = 0
        close = 0 
        res = []
        def dfs(open, close, s):
            print(s)
            if open > n:
                return 
            if open == close == n:
                res.append(s)
                return
            if open > close:
                dfs(open, close + 1, s + ")")
            dfs(open+1, close, s + "(")
        dfs(0,0,"")
        return res
