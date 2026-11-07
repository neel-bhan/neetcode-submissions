"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x:x.start)

        i = 0 
        heap = []
        res = 0
        while i < len(intervals):
            while heap and intervals[i].start >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, intervals[i].end)
            res = max(res, len(heap))
            i+=1
        return res
