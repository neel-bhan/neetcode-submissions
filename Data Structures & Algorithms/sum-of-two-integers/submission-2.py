class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = 0
        carry = 0
        mask = 0xFFFFFFFF

        for i in range(32):
            a1 = (a >> i) & 1
            b1 = (b >> i) & 1
            cur_bit = a1 ^ b1 ^ carry
            if((a1 and b1 and carry) or (a1 and b1) or (a1 and carry) or (b1 and carry)):
                carry = 1;
            else:
                carry = 0;

            if cur_bit:
                res |= (1 << i)
            
        if res > 0x7FFFFFFF:
            res = ~(res ^ mask)
        return res
