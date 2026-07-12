class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, r = 0, 0
        d = {}

        if(len(t) > len(s)):
            return ""

        for i in t:
            d[i] = d.get(i, 0) + 1

        left = len(set(t))
        ll, lr = 0, len(s)

        valid = False
        while r < len(s):
            if s[r] in d:
                d[s[r]] -= 1
                if d[s[r]] == 0:
                    left -= 1
            if left == 0:
                while left <= 0:
                    if lr - ll > r - l:
                        ll = l
                        lr = r
                        valid = True
                    if s[l] in d:
                        d[s[l]] += 1
                        if d[s[l]] > 0:
                            left += 1
                    l += 1
            r += 1
        return s[ll:lr+1] if valid else ""                
                

                    

        