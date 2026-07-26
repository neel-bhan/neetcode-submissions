class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][0] >= h:
                height, index = stack.pop()
                res = max(res, height * (i - index))
                start = index
            stack.append((h, start))

        while stack:
            height, index = stack.pop()
            res = max(res, height * (len(heights) - index))
        return res
        

        