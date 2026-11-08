class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = zip(position, speed)
        n = list(n)
        n.sort(reverse=True)

        stack = []

        res = 0
        prev = 0
        for p, s in n:
            time = (target - p) / s
            if not prev or prev < time:
                prev= time
                res += 1
        return res
