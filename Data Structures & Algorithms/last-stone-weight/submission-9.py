class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        

        if len(stones) == 1:
            return stones[0]
        for i in range(len(stones)):
            stones[i] *= -1
        heapq.heapify(stones)
        print(stones)
        while len(stones) > 1:
            s1 = heapq.heappop(stones)
            s2 = heapq.heappop(stones)

            value = abs(s1- s2)
            if value != 0:
                heapq.heappush(stones, -value)

        return 0 if len(stones) == 0 else -stones[0]
        