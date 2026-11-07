
class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def helper(num, power):
            if power <= 0:
                return 1
            if power == 1:
                return num
            if power % 2 == 0:
                return helper(num * num,  power // 2)
            else:
                return num * helper(num, power        -  1)
        if n < 0:
            return helper(1/x, -n)
        return helper(x, n)


        '''   
        helper(2, 5) - > 16
        helper(4, 2) -> 16
        helper(16, 1) -> 1'''