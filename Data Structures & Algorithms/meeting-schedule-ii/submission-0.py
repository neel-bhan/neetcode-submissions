"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        i = 0
        l, r = 0,0
        res = 0
        n = len(intervals)
        start = sorted(i.start for i in intervals)
        end = sorted(i.end for i in intervals)

        while l < n:
            if start[l] < end[r]:
                i+=1
                l+=1
                res = max(res, i)
            else:
                i -=1 
                r += 1
        return res

            

        

        



