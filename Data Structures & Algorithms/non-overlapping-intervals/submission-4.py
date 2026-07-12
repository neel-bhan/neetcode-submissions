class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        res = 0 
        i = 0 
        n = len(intervals)
        last= float("-inf")

        while i < n:
            if intervals[i][0] >= last:
                last = intervals[i][1]
            else:
                res += 1
            i+= 1
        return res