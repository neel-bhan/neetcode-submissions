class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        #sort queries also save index as q[1]
        #go through the modified interval list and keep adding to heapq until start of intervals[i] is bigger than the giver query and also pop until the end to is too early

        for i in range(len(queries)):
            queries[i] = (queries[i], i)
        queries.sort()
        res = []
        h = []
        j = 0
        h = []
        i =0 
        intervals.sort()
        while i < len(queries):

            num, _ = queries[i]
            while j < len(intervals) and intervals[j][0] <= num:
                heapq.heappush(h, (intervals[j][1] - intervals[j][0], intervals[j][1]))
                j += 1
            while h and h[0][1] < num:
                heapq.heappop(h)
            if h:
                res.append(h[0][0] + 1)
            else:
                res.append(-1)
            i += 1

        i = 0 
        j = 0
        ret = [0] * len(queries)
        for i in range(len(queries)):
            index = queries[i][1]
            ret[index] = res[i]
        return ret
