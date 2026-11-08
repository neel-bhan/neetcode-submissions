class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)
        h = []
        q = deque() #num, time
        res = 0
        for task, num in c.items():
            heapq.heappush(h, -num)

        while h or q:
            if not h:
                ele = q.popleft()
                res = ele[1]
                heapq.heappush(h, ele[0])
                
            ele = heapq.heappop(h)
            if ele + 1:
                q.append((ele + 1, res +1 +  n))

            res += 1
            if not h and not q:
                return res
            while q and q[0][1] <= res:
                heapq.heappush(h, q.popleft()[0])
        return res
