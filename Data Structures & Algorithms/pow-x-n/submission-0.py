class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def helper(num, power):
            if num == 0:
                return 0
            if power == 0:
                return 1
            res = helper(num * num, power // 2)
            return num * res if power % 2 else res
        ans = helper(x, abs(n))

        return ans if n >= 0 else 1/ans
            
        