class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = [] #height, index
        res = 0

        for index, h in enumerate(heights):
            start = index
            while stack and h <= stack[-1][0]:
                ph, pi = stack.pop()
                res = max(res, (index-pi) * ph)
                start = pi
            stack.append((h, start))

        while stack:
            ph, pi = stack.pop()
            res = max(res, (len(heights)-pi) * ph)

        return res
