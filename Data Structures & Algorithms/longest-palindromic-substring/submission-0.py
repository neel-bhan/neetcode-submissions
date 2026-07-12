class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        n = len(s)
        for index in range(n):
            cur = ""
            #odd
            i = index
            j = index 
            while i >= 0 and j < n:
                if s[i] == s[j]:
                    cur = s[i:j+1]
                    i-=1
                    j+=1
                else:
                    break
            if len(cur) > len(res):
                res = cur
            i = index
            j = index +1
            cur = ""
            while i >= 0 and j < n:
                if s[i] == s[j]:
                    cur = s[i:j+1] 
                    i-=1
                    j+=1
                else:
                    break   
            if len(cur) > len(res):
                res = cur
        return res
