class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  

        for index, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                i, temp = stack.pop()
                res[i] = index - i
            stack.append([index, t])
        return res