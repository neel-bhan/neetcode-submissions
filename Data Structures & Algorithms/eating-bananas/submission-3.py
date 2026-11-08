class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def speed(k):
            res =0 
            for p in piles:
                res += math.ceil(p/k)
            return res

        l, r= 1, max(piles)
        res = float('inf')
        while l <= r:
            m = (l + r) // 2
            v = speed(m)
            print(v)

            if v <= h:
                res = min(res,m)
                r = m -1
            else:
                l = m + 1
        return res
            

                
            