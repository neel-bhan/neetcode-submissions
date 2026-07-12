class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        chars = set(s)

        res = 0
        for i in chars:
            l,r = 0, 0
            ans = set()
            count = 0
            while r < len(s):
                if s[r] != i:
                    count += 1
                    if count > k:
                        while s[l] == i and l < r:
                            l+=1
                        l+=1
                        count -= 1
                res = max(res, r-l+ 1)
                r+=1
        return res       
                            
                


            
        