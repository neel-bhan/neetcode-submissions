class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0

        for index, h in enumerate(heights):
            mini = index
            while stack and h < stack[-1][1]:
                temp = stack.pop()
                mini = temp[0]
                res = max(res, (index - temp[0]) * temp[1])
            stack.append([mini, h])
        print(stack)
        while stack:
            temp = stack.pop()
            res = max(res, (len(heights) -temp[0])  * temp[1])

        return res

        

        