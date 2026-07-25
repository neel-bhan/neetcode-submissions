class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        if t == "":
            return ""
        sd = defaultdict(int)
        td = defaultdict(int)

        for i in t:
            td[i] += 1
        res = (-1,-1)
        reslen = float("inf")
        have, need = 0, len(td)
        for r in range(len(s)):
            ch = s[r]
            sd[ch] += 1
            if ch in td:
                if td[ch] == sd[ch]:
                    have += 1
            
            while have == need:
                if r-l+1 < reslen:
                    res = (l, r)
                    reslen = r-l+1
                sd[s[l]] -=1
                if s[l] in td and sd[s[l]] < td[s[l]]:
                    have -=1
                l+=1
        return s[res[0]:res[1]+1] if reslen != float("inf") else ""
                    


