"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x:x.start)
        i = 0
        last = float('-inf')
        while i < len(intervals):
            if intervals[i].start < last:
                return False
            last = intervals[i].end
            i += 1
        return True
