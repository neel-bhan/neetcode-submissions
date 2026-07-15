class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {}
        if len(s1) + len(s2) != len(s3):
            return False
        def dfs(l,r, i):

            if i == len(s3):
                return True
            if not(l in range(len(s1)) or r in range(len(s2))):
                return False
            if (l, r, i) in memo:
                return memo[(l, r, i)]
            if l < len(s1) and s1[l] == s3[i] and dfs(l+1, r, i+1):
                memo[(l, r, i)] = True
                return True
            if r < len(s2) and s2[r] == s3[i] and dfs(l, r+1, i+1):
                memo[(l, r, i)] =  True
                return True
            memo[(l, r, i)] = False
            return False
        return dfs(0,0,0)
        