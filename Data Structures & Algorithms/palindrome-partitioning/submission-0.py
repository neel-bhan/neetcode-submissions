class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPali(s):
            return s == s[::-1]
        
        subset = []
        res = []

        def dfs(cur, index):
            print(cur)
            print(index)
            print(subset)
            if index >= len(s):
                if not isPali(cur):
                    return
                subset.append(cur)
                res.append(subset.copy())
                subset.pop()
                return
                
            if isPali(cur) and index != 0:
                subset.append(cur)
                dfs(s[index], index + 1)
                subset.pop()
            cur += s[index]
            dfs(cur, index + 1)
        dfs("", 0)
        return res


