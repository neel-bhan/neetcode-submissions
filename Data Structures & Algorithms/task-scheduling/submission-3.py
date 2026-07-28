class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)
        h = []
        for k, v in c.items():
            heapq.heappush(h, (-v, k))
        r = deque()
        time = 0
        while h or r:
            if not h:
                time = r[0][0]
            while r and r[0][0] <= time:
                qt, qn,qv = r.popleft()
                heapq.heappush(h,(qn, qv))
            num, val = heapq.heappop(h)
            time += 1
            if -num-1 > 0:
                r.append((time + n, num +1, val))    


                

                
        return time