class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda pair: pair[1])
        res = 0
        lastend = -50000
        for inter in intervals:
            cs = inter[0]
            ce = inter[1]
            if cs >= lastend:
                lastend = ce
            else:
                res+=1
        return res
            




        