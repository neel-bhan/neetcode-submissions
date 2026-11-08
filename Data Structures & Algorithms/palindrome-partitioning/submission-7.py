class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        sub = []

        def dfs(i):
            def isp(s):
                i, j = 0, len(s)-1
                while i <= j:
                    if s[i] != s[j]:
                        return False
                    i += 1
                    j -=1
                return True
            if i >= len(s):
                res.append(sub.copy())
            for j in range(i+1, len(s)+1):
                if isp(s[i:j]):
                    sub.append(s[i:j])
                    dfs(j)
                    sub.pop()
        
        dfs(0)
        return res