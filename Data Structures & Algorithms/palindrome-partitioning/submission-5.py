class Solution:
    def partition(self, s: str) -> List[List[str]]:

        
        def isPali( s):
            l, r = 0, len(s)-1
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True

        res = [] 
        cur = []

        def dfs(i, cur_s):

            if i >= len(s):
                if cur_s == "":
                    res.append(cur.copy())
                return
            if isPali(str(cur_s + s[i])):
                cur.append(str(cur_s + s[i]))
                dfs(i+1, "")
                cur.pop()
                
           
            dfs(i+1, cur_s+ s[i])
            
        dfs(0,  "")
        return res

        