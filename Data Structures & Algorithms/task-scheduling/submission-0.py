from collections import defaultdict, deque
import heapq
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = defaultdict(int)
        for t in tasks:
            d[t] += 1

        pq = []
        for task, v in d.items():
            heapq.heappush(pq, (-v, task))  # tuple is cleaner than list

        time = 0
        q = deque()  # entries: (negCountRemaining, readyTime)

        while pq or q:
            time += 1

            if pq:
                negCnt, task = heapq.heappop(pq)
                negCnt += 1  # because it's negative; +1 means one less remaining
                if negCnt != 0:
                    q.append((negCnt, time + n))

            # if something's cooldown is over, put back in heap
            if q and q[0][1] == time:
                heapq.heappush(pq, (q.popleft()[0], task))

        return time