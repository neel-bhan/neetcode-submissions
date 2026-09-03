class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        indexs = []
        for index, i in enumerate(queries):
            indexs.append((i, index))
        queries = indexs
        queries.sort()
        i = 0
        cur = 0
        res = [[] for i in range(len(queries))]
        h = []

        intervals.sort()
        while cur < len(queries):
            ele = queries[cur][0]
            while i < len(intervals) and intervals[i][0] <= ele:
                heapq.heappush(h, (intervals[i][1] - intervals[i][0] + 1, i))
                i+=1
            
            while h and intervals[h[0][1]][1] < ele:
                heapq.heappop(h)

            if h:
                res[queries[cur][1]] = h[0][0]  
            else:
                res[queries[cur][1]] = -1
            cur+=1
        return res