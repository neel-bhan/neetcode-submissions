class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        lowest = max(piles)
        while l <= r:
            m = (l + r) // 2
            time = 0
            for b in piles:
                time += math.ceil(b / m)
            if time > h:
                l = m + 1
            else:
                lowest = min(lowest, m)
                r = m - 1
        return lowest