"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.end)
        res = 0 
        i = 0 
        n = len(intervals)
        last= float("-inf")

        while i < n:
            if intervals[i].start >= last:
                last = intervals[i].end
            else:
                return False
            i+= 1
        return True