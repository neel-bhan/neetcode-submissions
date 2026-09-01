class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        i = 0
        intervals.sort()
        print(res)
        while i < len(intervals):
            if res and res[-1][1] >= intervals[i][0]:
                res[-1][0] = min(res[-1][0], intervals[i][0])
                res[-1][1] = max(res[-1][1], intervals[i][1])
            else:
                res.append(intervals[i])
            i+=1
        return res