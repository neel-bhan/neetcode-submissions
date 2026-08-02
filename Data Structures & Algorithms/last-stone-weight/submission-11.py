class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for s in range(len(stones)):
            stones[s] *= -1
        heapq.heapify(stones)

        if len(stones) == 1:
            return -stones[0]
        while len(stones) >= 2:
            one = heapq.heappop(stones)
            two = heapq.heappop(stones)
            if one == two:
                continue
            heapq.heappush(stones, -abs(one - two))
        return -stones[0] if stones else 0