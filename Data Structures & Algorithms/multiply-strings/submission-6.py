class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]
        res = [0] * (len(num1) + len(num2))
        for i in range(len(num1)):
            for j in range(len(num2)):
                ans =  res[i+j] + (int(num1[i]) * int(num2[j]))
                res[i+j] = ans % 10
                res[i + j + 1] += ans // 10
        print(res)
        index = len(res)-1
        while index > 0 and res[index] == 0:
            index -= 1
        res = res[:index+1]
        for i in range(len(res)):
            res[i] = str(res[i])
        res = res[::-1]
        return "".join(res)
                
            

