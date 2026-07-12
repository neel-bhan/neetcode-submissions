class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]* len(temperatures)
        for index, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                print(stack)
                i, temp = stack.pop()
                res[i] = index  - i
            print(stack)
            stack.append([index, t])
        return res 
