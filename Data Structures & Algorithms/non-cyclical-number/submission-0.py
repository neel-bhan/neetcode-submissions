class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        #s.add(n)
        cur = 1
        i = 0
        while True:
            cur = 0
            while n != 0:
                cur += pow(n%10,2)
                n = n //10
            if cur == 1:
                return True
            if cur in s:
                return False
            s.add(cur)
            n = cur
            print(cur)

            
        