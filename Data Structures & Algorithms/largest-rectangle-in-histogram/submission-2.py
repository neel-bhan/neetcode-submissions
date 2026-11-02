class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = [] #index, height

        for i, h in enumerate(heights):
            start = i 
            while stack and stack[-1][1] >= h:
                index, height = stack.pop()
                res = max(res, (i - index) * height)
                start = index
            stack.append((start, h))

        while stack:
            index, height = stack.pop()
            res = max(res, (len(heights) - index) * height)
        
        return res



        

        