class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxh = 0
        l, r = 0, len(heights) - 1

        maxh = max(maxh, min(heights[l], heights[r]) * (r-l))

        while r > l:
            if heights[l] < heights[r]:
                l +=1
            else:
                r-=1
            maxh = max(maxh, min(heights[l], heights[r]) * (r-l))

        return maxh

        