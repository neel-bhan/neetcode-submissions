class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        subset = []
        res = []

        def dfs(o, c):
            if o == c == n:
                res.append("".join(subset))
                return
            if o < n:
                subset.append('(')
                dfs(o+1, c)
                subset.pop()
            if o > c:
                subset.append(')')
                dfs(o, c + 1)
                subset.pop()
        dfs(0,0)
        return res
            
        